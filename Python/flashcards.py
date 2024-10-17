import tkinter as tk
from tkinter import messagebox
import random
from tkinter import simpledialog 
# Flashcards dictionary to store term and definition
flashcards = {}

# Function to add flashcards
def add_flashcard():
    term = entry_term.get()
    definition = entry_definition.get()

    if term and definition:
        flashcards[term] = definition
        messagebox.showinfo("Success", f"Flashcard '{term}' added!")
        entry_term.delete(0, tk.END)
        entry_definition.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both term and definition.")

# Function to view flashcards
def view_flashcards():
    if flashcards:
        flashcard_text = "\n".join([f"{term}: {definition}" for term, definition in flashcards.items()])
        messagebox.showinfo("Flashcards", flashcard_text)
    else:
        messagebox.showwarning("No Flashcards", "No flashcards to show!")

# Function to quiz user on flashcards
def quiz():
    if flashcards:
        term = random.choice(list(flashcards.keys()))
        definition = flashcards[term]

        answer = simpledialog.askstring("Quiz", f"What is the definition of '{term}'?")
        
        if answer and answer.lower() == definition.lower():
            messagebox.showinfo("Correct", "You got it right!")
        else:
            messagebox.showinfo("Incorrect", f"The correct definition is '{definition}'.")
    else:
        messagebox.showwarning("No Flashcards", "No flashcards to quiz!")

# Setting up the main window
root = tk.Tk()
root.title("Flashcard App")
root.geometry("400x300")

# Labels
label_term = tk.Label(root, text="Enter Term:")
label_term.pack()

# Entry for term
entry_term = tk.Entry(root)
entry_term.pack()

label_definition = tk.Label(root, text="Enter Definition:")
label_definition.pack()

entry_definition = tk.Entry(root)
entry_definition.pack()

# Add Flashcard Button
btn_add = tk.Button(root, text="Add Flashcard", command=add_flashcard)
btn_add.pack(pady=10)

# View Flashcards Button
btn_view = tk.Button(root, text="View Flashcards", command=view_flashcards)
btn_view.pack(pady=10)

# Quiz Button
btn_quiz = tk.Button(root, text="Start Quiz", command=quiz)
btn_quiz.pack(pady=10)

root.mainloop()
