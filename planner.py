import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

# Add task
def add_task():
    task = task_entry.get()
    deadline = deadline_entry.get()
    priority = priority_var.get()

    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    tasks.append({"task": task, "deadline": deadline, "priority": priority, "done": False})
    update_list()
    save_tasks()

    task_entry.delete(0, tk.END)
    deadline_entry.delete(0, tk.END)

# Mark done
def mark_done():
    try:
        index = listbox.curselection()[0]
        tasks[index]["done"] = True
        update_list()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task first!")

# Delete task
def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        update_list()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task first!")

# Update display
def update_list():
    listbox.delete(0, tk.END)
    for t in tasks:
        status = "✔" if t["done"] else "❌"
        text = f"{status} {t['task']} | Due: {t['deadline']} | Priority: {t['priority']}"
        listbox.insert(tk.END, text)

# GUI setup
root = tk.Tk()
root.title("Smart Student Planner")
root.geometry("500x500")

tasks = load_tasks()

tk.Label(root, text="Task").pack()
task_entry = tk.Entry(root, width=40)
task_entry.pack()

tk.Label(root, text="Deadline").pack()
deadline_entry = tk.Entry(root, width=40)
deadline_entry.pack()

tk.Label(root, text="Priority").pack()
priority_var = tk.StringVar(value="Medium")
priority_menu = tk.OptionMenu(root, priority_var, "High", "Medium", "Low")
priority_menu.pack()

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Mark Done", command=mark_done).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)

listbox = tk.Listbox(root, width=70, height=15)
listbox.pack(pady=10)

update_list()

root.mainloop()