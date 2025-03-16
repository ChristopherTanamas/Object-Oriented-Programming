from app.services import TaskManagerService
from app.persistances import TaskManagerDB
from app.observer import Subject, Subscriber
from app.dtos import TaskManagerDTO
import sqlite3
from queue import PriorityQueue
from kink import inject, di
import os

@inject
class MockTaskManagerDB(TaskManagerDB):
    def __init__(self, _db_file, dbunit):
        self.db_file = _db_file
        self.conn = sqlite3.connect(self.db_file)
        self.create_table()
    
    def select_all_task(self):
        all_task_name = []
        all_task_date = []
        all_task_hour = []
        res = self.conn.execute("SELECT * FROM mock_task_manager")
        result = res.fetchall()

        q = PriorityQueue()

        for task in result:
            q.put((task[1] , task[2], task[0]))

        while len(q.queue) != 0:
            task = q.get()
            all_task_name.append(task[2])
            all_task_date.append(task[0])
            all_task_hour.append(task[1])
        return TaskManagerDTO(all_task_name, all_task_date, all_task_hour)

    def create_table(self):
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS mock_task_manager(task_name varchar (30), due_date date, due_time time)")
        self.conn.commit()

    def add_task(self, _task_name, _task_due_date, _task_due_time):
        time = _task_due_time + ':00'
        self.conn.execute(f"INSERT INTO mock_task_manager values('{_task_name}', '{_task_due_date}', '{time}')")
        self.conn.commit()

    def drop_task(self, _task_name):
        self.conn.execute(f"DELETE FROM mock_task_manager WHERE task_name = '{_task_name}'")
        self.conn.commit()

@inject
class MockObserver(Subscriber):
    def notified(self, _task_name, _task_due_date, _task_due_time):
        all_task = []
        conn = sqlite3.connect('Mock_Database.db')
        cur =  conn.execute("SELECT task_name FROM mock_task_manager")
        result = cur.fetchall()
        conn.close()
        for task_name in result:
            all_task.append(task_name[0])
        return all_task

@inject
class MockSubject(Subject):
    def __init__(self, _observers:MockObserver):
        self.observers = _observers

    def add_observer(self, _observer):
        pass

    def remove_observer(self, _observer):
        pass

    def notify(self, _task_name, _task_due_date, _task_due_time):
        return self.observers.notified(_task_name, _task_due_date, _task_due_time)

def test_single_tone():
    di['_db_file'] = "Mock_Database.db"
    di['dbunit'] = 'True'

    di[TaskManagerDB] = MockTaskManagerDB()
    di[Subject] = MockSubject()

    service = di[TaskManagerService]
    service.add_task('UAS OOP','2023-18-12','23:59')
    service_task_name = service.show_all_task().task_name

    subject_task_name = service.subject.notify('test','test','test')
    
    assert service_task_name == subject_task_name, f"Expect : {service_task_name}, but get Current : {subject_task_name}"
    closed = service.task_manager_db.conn
    closed.close()
    os.remove("./Mock_Database.db")


if __name__ == '__main__':
    test_single_tone()