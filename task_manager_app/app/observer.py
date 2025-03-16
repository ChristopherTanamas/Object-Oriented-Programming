from abc import ABC
from abc import abstractmethod
from tkinter.messagebox import showinfo
from datetime import datetime
import sqlite3
from queue import PriorityQueue
from kink import inject


class Subscriber(ABC):
    @abstractmethod
    def notified(self, _task_name, _task_due_date, _task_due_time):
        pass


class Subject(ABC):
    @abstractmethod
    def __init__(self, _observers):
        pass

    def add_observer(self, _observer):
        pass

    def remove_observer(self, _observer):
        pass

    def notify(self, _task_name, _task_due_date, _task_due_time):
        pass


@inject(alias=Subscriber)
class WarningSameTask(Subscriber):
    def notified(self, _task_name, _task_due_date, _task_due_time):
        all_task = []
        conn = sqlite3.connect('Task Reminder.db')
        cur =  conn.execute("SELECT task_name FROM task_manager")
        result = cur.fetchall()
        for task_name in result:
            all_task.append(task_name[0])
        
        if _task_name in all_task:
            return showinfo(title="Submitting Failed", message=f"There is already a task named {_task_name}!\n Please input another task name!")

@inject(alias=Subscriber)
class NotifyEvery5Tasks(Subscriber):
    def notified(self, _task_name, _task_due_date, _task_due_time):
        conn = sqlite3.connect('Task Reminder.db')
        cur =  conn.execute("SELECT task_name FROM task_manager")
        all_task = cur.fetchall()

        if (len(all_task)+1) % 5 == 0:
            return showinfo(title="Warning!", message=f"Be Careful!\n You already have {len(all_task)+1} tasks remaining!\n Don't forget to do your task!")

@inject(alias=Subscriber)
class NotifyClosestDeadline(Subscriber):
    def notified(self, _task_name, _task_due_date, _task_due_time):
        q = PriorityQueue()
        conn = sqlite3.connect('Task Reminder.db')
        cur =  conn.execute("SELECT * FROM task_manager")
        res = cur.fetchall()
        result = []

        for data in res:
            result.append((data[1],data[2],data[0]))

        for task_name in result:
            q.put(task_name)
        
        if len(q.queue) != 0:
            closest = q.queue[0]
            due_date_time = datetime.strptime(closest[0] + ' ' + closest[1] , "%Y-%m-%d %H:%M:%S")
            current_time = datetime.now()

            total_second = (due_date_time - current_time).total_seconds()
            hours = int(total_second // (60*60))
            minutes = int((total_second - (hours * (60*60))) // 60)
            seconds = int(total_second - hours * (60 * 60) - minutes * 60)

            return showinfo(title="Closest Deadline", message=f"Task with the closest deadline!\n{closest[0]} must be submitted before {closest[1]}\nTime Remaining: {hours} hours {minutes} minutes {seconds} seconds")

@inject(alias= Subject)
class TaskManagerSubject(Subject):
    def __init__(self, _observers:list[Subscriber]):
        self.observers = _observers

    def add_observer(self, _observer):
        self.observers.append(_observer)

    def remove_observer(self, _observer):
        self.observers.remove(_observer)

    def notify(self, _task_name, _task_due_date, _task_due_time):
        for observer in self.observers:
            observer.notified(_task_name, _task_due_date, _task_due_time)