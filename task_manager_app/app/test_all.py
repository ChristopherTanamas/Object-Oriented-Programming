from app.persistances import TaskManagerDB
from app.observer import TaskManagerSubject
from app.services import TaskManagerService
from app.dtos import TaskManagerDTO

# Mock TaskManagerDB for testing purposes
class MockTaskManagerDB(TaskManagerDB):
    def __init__(self, _db_file, dbunit):
        pass

    def select_all_task(self):
        # Return some test data for the purpose of the test
        return TaskManagerDTO(["Task 1", "Task 2"], ["2023-01-01", "2023-01-02"], ["12:00", "14:00"])

def test_show_all_task():
    # Pembuatan mock_db dan juga service
    mock_db = MockTaskManagerDB("testing_file_db", dbunit="False")
    service = TaskManagerService(mock_db, TaskManagerSubject())

    # Panggil semua task buat mengetahui hasil isinya
    current = service.show_all_task()

    # Meng-set ekspetasi daripada hasil
    expected = TaskManagerDTO(["Task 1", "Task 2"], ["2023-01-01", "2023-01-02"], ["12:00", "14:00"])

    # Meng-check jika current == expected
    assert current.task_name == expected.task_name
    assert current.task_date == expected.task_date
    assert current.task_hour == expected.task_hour


if __name__ == "__main__":
    test_show_all_task()