import tkinter as tk
from tkinter import messagebox
import datetime


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, deadline):
        task = Task(name, deadline)
        self.tasks.append(task)

    def get_days_until_deadline(self, task):
        current_date = datetime.date.today()
        days_left = (task.deadline - current_date).days
        return days_left


class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline

    def __str__(self):
        return self.name


def open_calendar():
    # Papildyti funkcionalumą kalendoriui
    pass


def open_task_management():
    task_management_window = tk.Toplevel(root)
    task_management_window.title("Darbų valdymas")

    frame_task_input = tk.Frame(task_management_window)
    frame_task_input.pack(pady=10)

    label_task_name = tk.Label(frame_task_input, text="Darbo pavadinimas:")
    label_task_name.grid(row=0, column=0, padx=5, pady=5)

    entry_task_name = tk.Entry(frame_task_input)
    entry_task_name.grid(row=0, column=1, padx=5, pady=5)

    label_task_deadline = tk.Label(frame_task_input, text="Terminas (YYYY-MM-DD):")
    label_task_deadline.grid(row=1, column=0, padx=5, pady=5)

    entry_task_deadline = tk.Entry(frame_task_input)
    entry_task_deadline.grid(row=1, column=1, padx=5, pady=5)

    def add_task():
        name = entry_task_name.get()
        deadline = entry_task_deadline.get()

        if name and deadline:
            try:
                deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d").date()
                task_manager.add_task(name, deadline)
                entry_task_name.delete(0, tk.END)
                entry_task_deadline.delete(0, tk.END)
                update_task_list()  # Atnaujiname darbų sąrašą po darbo pridėjimo
            except ValueError:
                messagebox.showerror("Klaida", "Neteisingas datos formatas. Pateikite datą formato YYYY-MM-DD.")
        else:
            messagebox.showerror("Klaida", "Užpildykite visus laukus!")

    button_add_task = tk.Button(frame_task_input, text="Pridėti darbą", command=add_task)
    button_add_task.grid(row=2, columnspan=2, pady=10)

    frame_task_list = tk.Frame(task_management_window)
    frame_task_list.pack(pady=10)

    label_task_list = tk.Label(frame_task_list, text="Darbų sąrašas:")
    label_task_list.pack()

    listbox_tasks = tk.Listbox(frame_task_list, width=50)
    listbox_tasks.pack(pady=5)

    def update_task_list():
        listbox_tasks.delete(0, tk.END)
        for task in task_manager.tasks:
            days_left = task_manager.get_days_until_deadline(task)
            task_info = f"{task.name} (Terminas: {task.deadline}, liko dienų: {days_left})"
            listbox_tasks.insert(tk.END, task_info)

    task_manager = TaskManager()

    root.wait_window(task_management_window)


root = tk.Tk()
root.title("Darbų planavimo ir laiko valdymo programa")

frame_intro = tk.Frame(root)
frame_intro.pack(pady=20)

label_intro = tk.Label(frame_intro, text="Sveiki! Tai yra darbų planavimo ir laiko valdymo programa.")
label_intro.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_calendar = tk.Button(frame_buttons, text="Kalendorius", command=open_calendar)
button_calendar.grid(row=0, column=0, padx=10)

button_task_management = tk.Button(frame_buttons, text="Darbų valdymas", command=open_task_management)
button_task_management.grid(row=0, column=1, padx=10)

root.mainloop()
