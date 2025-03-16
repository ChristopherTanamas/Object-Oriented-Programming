from app.persistances import TaskManagerDB
from app.observer import Subject
from kink import inject

@inject
class TaskManagerService:
    def __init__(self,_task_manager_db:TaskManagerDB, _task_notification_subject: Subject):
        self.task_manager_db = _task_manager_db
        self.subject = _task_notification_subject

    def show_all_task(self):
        return self.task_manager_db.select_all_task()
    
    def add_task(self,_task_name, _task_due_date, _task_due_time):
        self.subject.notify(_task_name, _task_due_date, _task_due_time)
        if _task_name not in self.show_all_task().task_name:
            return self.task_manager_db.add_task(_task_name, _task_due_date, _task_due_time)

    def drop_task(self,_task_name):
        return self.task_manager_db.drop_task(_task_name)