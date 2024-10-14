import tkinter as tr
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("Python File", "*.py"), ("C++ File", "*.cpp")])
    
    if not filepath:
        return
    
    text_edit.delete(1.0, tr.END)  # 1.0 = Line 1 and 0th Character
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tr.END, content)
    window.title(f"Open File: {filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("Python File", "*.py"), ("C++ File", "*.cpp")])
    
    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tr.END)
        f.write(content)
    window.title(f"Saved File: {filepath}")

def main():
    window = tr.Tk()
    window.title("Text Editor: Made Using Python")
    window.rowconfigure(0, minsize=100)
    window.columnconfigure(1, minsize=100)

    text_edit = tr.Text(window, font="Helvetica 11 bold")
    text_edit.grid(row=0, column=1)

    Frame = tr.Frame(window, relief=tr.RAISED, bd=2)
    save_button = tr.Button(Frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tr.Button(Frame, text="Open", command=lambda: open_file(window, text_edit))

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    Frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    window.mainloop()

if __name__ == "__main__":
    main()
