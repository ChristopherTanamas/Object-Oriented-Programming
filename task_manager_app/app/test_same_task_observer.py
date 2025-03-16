from app.observer import Subscriber
import sqlite3
import os

class MockWarningSameTask(Subscriber):
    def notified(self, _task_name, _task_due_date, _task_due_time):
        all_task = []
        conn = sqlite3.connect('Mock_Database.db')
        cur =  conn.execute("SELECT task_name FROM mock_task_manager")
        result = cur.fetchall()
        conn.close()
        for task_name in result:
            all_task.append(task_name[0])
        
        if _task_name in all_task:
            return f"{_task_name} is doubled"

def test_warning_same_task():
    conn = sqlite3.connect('Mock_Database.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mock_task_manager(task_name varchar (30), due_date date, due_time time)")
    cur.execute("INSERT INTO mock_task_manager VALUES ('UAS OOP','2023-18-12','23:59:00')")
    conn.commit()

    warning_same_task_test = MockWarningSameTask()
    current = warning_same_task_test.notified('UAS OOP','2023-18-12','23:59:00')

    expected = f"UAS OOP is doubled"

    assert current == expected, f"Expect : {expected}, but get Current : {current}"
    conn.close()
    os.remove("./Mock_Database.db")

if __name__ == '__main__':
    test_warning_same_task()