from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import re

root = Tk()
root.title("Marks Chart Generator")
root.geometry("600x500")
root.configure(bg='#f0f0f0')  # Light gray background

f = ("Calibri", 16)
entry_f = ("Calibri", 14)
button_f = ("Calibri", 16, "bold")

def validate_name(name):
    # Validate that the name contains only alphabetic characters. 
    return name.isalpha()

def validate_marks(marks):
    # Validate that the marks are integers. 
    return marks.isdigit()

def gen():
    name = ent_name.get().strip()
    physics = ent_physics.get().strip()
    chemistry = ent_chemistry.get().strip()
    maths = ent_maths.get().strip()
    
    # Validate name
    if not validate_name(name):
        messagebox.showerror("Input Error", "Invalid name. Only letters are allowed.")
        return
    
    # Validate marks
    if not (validate_marks(physics) and validate_marks(chemistry) and validate_marks(maths)):
        messagebox.showerror("Input Error", "Invalid marks. Only integers are allowed.")
        return
    
    # Convert marks to integers
    physics = int(physics)
    chemistry = int(chemistry)
    maths = int(maths)
    
    subjects = ["Physics", "Chemistry", "Maths"]
    marks = [physics, chemistry, maths]
    
    plt.bar(subjects, marks, color=['#4CAF50', '#FFC107', '#2196F3'], width=0.6)
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title(f"{name}'s Marks")
    plt.savefig("marks.pdf")
    plt.show()

# Frame for the form
frame = Frame(root, bg='#ffffff', padx=20, pady=20, relief=RAISED, borderwidth=2)
frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

# Labels and Entries
Label(frame, text="Enter Student Name:", font=f, bg='#ffffff').grid(row=0, column=0, padx=10, pady=10, sticky=W)
ent_name = Entry(frame, font=entry_f, width=30)
ent_name.grid(row=0, column=1, padx=10, pady=10)

Label(frame, text="Physics Marks:", font=f, bg='#ffffff').grid(row=1, column=0, padx=10, pady=10, sticky=W)
ent_physics = Entry(frame, font=entry_f, width=30)
ent_physics.grid(row=1, column=1, padx=10, pady=10)

Label(frame, text="Chemistry Marks:", font=f, bg='#ffffff').grid(row=2, column=0, padx=10, pady=10, sticky=W)
ent_chemistry = Entry(frame, font=entry_f, width=30)
ent_chemistry.grid(row=2, column=1, padx=10, pady=10)

Label(frame, text="Maths Marks:", font=f, bg='#ffffff').grid(row=3, column=0, padx=10, pady=10, sticky=W)
ent_maths = Entry(frame, font=entry_f, width=30)
ent_maths.grid(row=3, column=1, padx=10, pady=10)

btn_generate = Button(root, text="Generate Chart", font=button_f, bg='#4CAF50', fg='white', command=gen)
btn_generate.pack(pady=20)

root.mainloop()
