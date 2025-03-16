from abc import ABC
import sqlite3
from queue import PriorityQueue
from kink import inject
import os
from app.dtos import TaskManagerDTO


class TaskManagerDB(ABC):
    # Set up semua tabel dan data yang dibutuhkan
    def __init__(self, _db_file, dbunit): 
        pass

    def create_table(self):
        pass

    def select_all_task(self):
        pass

    def add_task(self, _task_name, _task_due_date, _task_due_time):
        pass

    def drop_task(self, _task_name):
        pass

@inject(alias= TaskManagerDB)
class TaskManagerSqlliteDB(TaskManagerDB):
    def __init__(self, _db_file, dbunit):
        self.db_file = _db_file
        self.conn = None
        if dbunit == 'True':
            os.remove(f"./{_db_file}.db")
            # inisialisasi connection
            self.conn = sqlite3.connect(f"{self.db_file}.db")
            self.create_table()
        elif dbunit == 'False' :
            self.conn = sqlite3.connect(f"{self.db_file}.db")
            self.create_table()

    def create_table(self):
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS task_manager(task_name varchar (30), due_date date, due_time time)")
        self.conn.commit()

    def select_all_task(self):
        all_task_name = []
        all_task_date = []
        all_task_hour = []
        res = self.conn.execute("SELECT * FROM task_manager")
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
    
    def add_task(self, _task_name, _task_due_date, _task_due_time):
        time = _task_due_time + ':00'
        self.conn.execute(f"INSERT INTO task_manager values('{_task_name}', '{_task_due_date}', '{time}')")
        self.conn.commit()

    def drop_task(self, _task_name):
        self.conn.execute(f"DELETE FROM task_manager WHERE task_name = '{_task_name}'")
        self.conn.commit()