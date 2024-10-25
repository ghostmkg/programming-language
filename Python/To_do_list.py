import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def delete_task():
    try:
        task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

def mark_task_complete():
    try:
        task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(task_index)
        tasks_listbox.delete(task_index)
        tasks_listbox.insert(tk.END, f"{task} (Completed)")
    except:
        messagebox.showwarning("Selection Error", "Please select a task to mark as complete!")

# Create the main window
window = tk.Tk()
window.title("To-Do List App")

# Create the task entry widget
task_entry = tk.Entry(window, width=40)
task_entry.pack(pady=10)

# Create the buttons
add_button = tk.Button(window, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

complete_button = tk.Button(window, text="Mark Task Complete", width=20, command=mark_task_complete)
complete_button.pack(pady=5)

# Create the listbox to display tasks
tasks_listbox = tk.Listbox(window, height=10, width=50)
tasks_listbox.pack(pady=10)

# Run the application
window.mainloop()
