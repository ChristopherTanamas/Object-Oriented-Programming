from app.persistances import TaskManagerDB
from app.persistances import TaskManagerSqlliteDB
from app.services import TaskManagerService
from app.UI import TaskManagerUI
from kink import di
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-dbunit')
    args = parser.parse_args()
    status_dbunit = args.dbunit.split(',')[0]

    di['_db_file'] = 'Task Reminder'
    di['dbunit'] = status_dbunit
    di[TaskManagerDB] = TaskManagerSqlliteDB()
    container = di[TaskManagerUI]
    container.show()

if __name__ == '__main__':
    main()