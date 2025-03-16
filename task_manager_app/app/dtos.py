from kink import inject

@inject
class TaskManagerDTO:
    def __init__(self,_task_name,_task_date, _task_hour):
        self.task_name = _task_name
        self.task_date = _task_date
        self.task_hour = _task_hour