from tkinter import *
from abc import ABC
from kink import inject
from app.services import TaskManagerService

class UI(ABC):
    def __init__(self, _task_manager_service: TaskManagerService):
        pass

    def get_task(self):
        pass

    def add_task(self):
        pass

    def drop_task(self):
        pass

    def main_GUI(self):
        pass

    def reminder_GUI(self):
        pass

    def reminder_delete(self):
        pass

    def reminder_list(self):
        pass

    def show(self):
        pass

@inject
class TaskManagerUI(UI):
    def __init__(self, _task_manager_service: TaskManagerService):
        self.reminder_ui = _task_manager_service
        self.all_tasks_names = []
        self.all_tasks_dates = []
        self.all_tasks_hours = []

    def get_tasks(self):
        list_task = self.reminder_ui.show_all_task()
        self.all_tasks_names = list_task.task_name
        self.all_tasks_dates = list_task.task_date
        self.all_tasks_hours = list_task.task_hour

    def add_task(self, _task_name, _task_due_date, _task_due_time):
        return self.reminder_ui.add_task(_task_name, _task_due_date, _task_due_time)

    def drop_task(self, _task_name):
        return self.reminder_ui.drop_task(_task_name)

    def main_GUI(self):
        main_window = Tk()
        main_window.title("Task Manager")
        main_window.geometry('500x200')
        main_window.resizable(False, False)

        main_frame = Frame(main_window, borderwidth=2)
        main_frame.pack()

        # Title
        font_tuple = ("Times", 20, "bold")
        task_name = Label(main_window, text="Select Your Choice!")
        task_name.configure(font=font_tuple)
        task_name.pack()
        task_name.place(x=130, y=15)

        ## Insert Task Button
        def insert_task_command():
            main_window.destroy()
            self.reminder_GUI().mainloop()

        reminder_button = Button(main_window, text="Insert Task", command=insert_task_command, fg='limegreen')
        reminder_button.pack()
        reminder_button.place(x=85, y=75)

        ## Delete Task Button
        def delete_task_command():
            main_window.destroy()
            self.reminder_delete().mainloop()

        delete_button = Button(main_window, text="Delete Task", command=delete_task_command, fg='crimson')
        delete_button.pack()
        delete_button.place(x=210, y=75)

        ## Tasks List Button
        def tasks_list_command():
            main_window.destroy()
            self.reminder_list().mainloop()

        tasks_list_button = Button(main_window, text="Tasks List", command=tasks_list_command, fg='midnightblue')
        tasks_list_button.pack()
        tasks_list_button.place(x=345, y=75)

        ## Exit Button
        exit_button = Button(main_window, text="Exit", command=main_window.destroy, width=20, fg='firebrick1')
        exit_button.pack()
        exit_button.place(x=170, y=125)

        return main_window

    ## I N S E R T  T A S K ##
    def reminder_GUI(self):
        self.get_tasks()
        reminder_window = Tk()
        reminder_window.title("Task Reminder")
        reminder_window.geometry('500x200')
        reminder_window.resizable(False, False)

        main_frame = Frame(reminder_window)
        main_frame.pack()

        # Title
        font_tuple = ("Times", 18, "bold")
        task_title = Label(reminder_window, text="Insert Your Task!")
        task_title.configure(font=font_tuple)
        task_title.pack()
        task_title.place(x=170, y=15)

        task_name = Label(reminder_window, text="Task Name")
        task_name.pack()
        task_name.place(x=30, y=50)
        task_name_box = Entry(reminder_window, width=40)
        task_name_box.pack()
        task_name_box.place(x=150, y=50)

        ## due date section ##
        task_due_date = Label(reminder_window, text="Task Due Date")
        task_due_date.pack()
        task_due_date.place(x=30, y=80)

        def temp_text_date(a):
            task_due_date_box.delete(0, "end")

        task_due_date_box = Entry(reminder_window, width=40)
        task_due_date_box.insert(0, "YYYY-MM-DD")
        task_due_date_box.pack()
        task_due_date_box.place(x=150, y=80)
        task_due_date_box.bind("<Button-1>", temp_text_date)

        # due time section ##
        task_due_time = Label(reminder_window, text="Task Due Time")
        task_due_time.pack()
        task_due_time.place(x=30, y=110)

        def temp_text_time(b):
            task_due_time_box.delete(0, "end")

        task_due_time_box = Entry(reminder_window, width=40)
        task_due_time_box.insert(0, "00:00")
        task_due_time_box.pack()
        task_due_time_box.place(x=150, y=110)
        task_due_time_box.bind("<Button-1>", temp_text_time)

        ## reminder fail ##
        def clearing_entry_box_reminder():
            task_due_date_box.delete(0, 'end')
            task_due_time_box.delete(0, 'end')
            task_name_box.delete(0, 'end')

        cancel_reminder = Button(reminder_window, text="Clear!", fg='midnightblue', command=clearing_entry_box_reminder)
        cancel_reminder.pack()
        cancel_reminder.place(x=30, y=150)

        ## reminder success ##
        def submitting_reminder():
            _task_name = task_name_box.get()
            _due_date = task_due_date_box.get()
            _due_time = task_due_time_box.get()
            self.add_task(_task_name, _due_date, _due_time)
            reminder_window.destroy()
            self.main_GUI()

        submit_reminder = Button(reminder_window, text="Remind Me!", fg='limegreen', command=submitting_reminder)
        submit_reminder.pack()
        submit_reminder.place(x=180, y=150)

        ## reminder exit ##
        def back_to_main():
            reminder_window.destroy()
            self.main_GUI().mainloop()

        quit_reminder = Button(reminder_window, text="Back!", fg='crimson', command=back_to_main)
        quit_reminder.pack()
        quit_reminder.place(x=365, y=150)

        return reminder_window

    ## D E L E T E  T A S K ##
    def reminder_delete(self):
        to_delete_window = Tk()
        to_delete_window.title("Task Reminder")
        to_delete_window.geometry('500x220')
        to_delete_window.resizable(False, False)

        to_delete_frame = Frame(to_delete_window)
        to_delete_frame.pack()

        ## T I T L E ##
        font_tuple = ("Times", 18, "bold")
        title_name = Label(to_delete_window, text="Delete Your Task!")
        title_name.configure(font=font_tuple)
        title_name.pack()
        title_name.place(x=160, y=15)

        ## S U B T I T L E"
        font_tuple_sub = ("Times", 14)
        subtitle_name = Label(to_delete_window, text="If you're already done the task, you can delete it.")
        subtitle_name.configure(font=font_tuple_sub)
        subtitle_name.pack()
        subtitle_name.place(x=65, y=50)

        ## D E L E T E
        def temp_text_name(a):
            task_name_box.delete(0, "end")

        task_name_box = Entry(to_delete_window, width=40)
        task_name_box.insert(0, "Enter Your Task Name")
        task_name_box.pack()
        task_name_box.place(x=130, y=100)
        task_name_box.bind("<Button-1>", temp_text_name)

        ## delete success ##
        def deleting_reminder():
            _task_name = task_name_box.get()
            self.drop_task(_task_name)
            to_delete_window.destroy()
            self.reminder_list().mainloop()

        delete_reminder = Button(to_delete_window, text="Delete!", fg= 'crimson', command=deleting_reminder)
        delete_reminder.pack()
        delete_reminder.place(x=225, y=130)

        ## B A C K ##
        def back_to_main():
            to_delete_window.destroy()
            self.main_GUI()

        back_from_list = Button(to_delete_window, text="<<", command=back_to_main, fg='midnightblue')
        back_from_list.pack()
        back_from_list.place(x=30, y=175)

        return to_delete_window

    ## T A S K S  L I S T ##
    def reminder_list(self):
        list_window = Tk()
        list_window.title("Task Reminder")
        list_window.geometry('500x500')
        list_window.resizable(False, False)

        main_frame = Frame(list_window)
        main_frame.pack()

        ## T I T L E ##
        font_tuple = ("Times", 18, "bold")
        title_name = Label(list_window, text="List of Tasks")
        title_name.configure(font=font_tuple)
        title_name.pack()
        title_name.place(x=180, y=15)

        ## S U B T I T L E"
        font_tuple_sub = ("Times", 14)
        subtitle_name = Label(list_window, text="Chill... we are ready to remind you of all Your tasks!")
        subtitle_name.configure(font=font_tuple_sub)
        subtitle_name.pack()
        subtitle_name.place(x=55, y=50)

        y_axis = 100
        font_tuple = ("Times", 10)

        self.get_tasks()


        for i in range (len(self.all_tasks_names)):
            task_due_date = Label(list_window, text=self.all_tasks_dates[i])
            task_due_date.configure(font=font_tuple)
            task_due_date.pack()
            task_due_date.place(x=30, y=y_axis)

            task_due_hour = Label(list_window, text=self.all_tasks_hours[i])
            task_due_hour.configure(font=font_tuple)
            task_due_hour.pack()
            task_due_hour.place(x=100, y=y_axis)

            task_name = Label(list_window, text=self.all_tasks_names[i])
            task_name.configure(font=font_tuple)
            task_name.pack()
            task_name.place(x=160, y=y_axis)

            y_axis += 30

        ## B A C K ##
        def back_to_main() :
            list_window.destroy()
            self.main_GUI()

        back_from_list = Button(list_window, text="<<", command=back_to_main, fg='midnightblue')
        back_from_list.pack()
        back_from_list.place(x=30, y=445)

        return list_window
    
    def show(self):
        self.main_GUI().mainloop()