import tkinter as tk
from tkinter import messagebox

def click_button(value):
    """Adds the clicked value (number or operator) to the entry field."""
    current = entry.get()
    
    if not current and value in '+-*/.':
        return
    if current and current[-1] in '+-*/.' and value in '+-*/.':
        if value in '+-*/':
            entry.delete(len(current) - 1, tk.END)
            entry.insert(tk.END, value)
        elif value == '.':
            return
    else:
        entry.insert(tk.END, value)

def clear():
    """Clears the entire entry field."""
    entry.delete(0, tk.END)

def calculate():
    """Calculates the result of the expression in the entry field."""
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Div/0 Error")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("340x450")
root.resizable(False, False) 
root.configure(bg="#2c3e50")
FONT_STYLE = ('Arial', 18, 'bold')
BG_DEFAULT = '#34495e'
FG_DEFAULT = 'white'
BG_OPERATOR = '#e67e22'
BG_EQUALS = '#27ae60'
BG_CLEAR = '#e74c3c'
entry = tk.Entry(
    root, 
    width=15, 
    font=('Arial', 24), 
    borderwidth=5, 
    relief="flat", 
    justify="right",
    bg="#ecf0f1",
    fg="#2c3e50"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")
buttons_data = [
    ('C', 1, 0, 1, BG_CLEAR, clear),
    ('/', 1, 3, 1, BG_OPERATOR, lambda: click_button('/')),
    ('7', 2, 0, 1, BG_DEFAULT, lambda: click_button('7')), 
    ('8', 2, 1, 1, BG_DEFAULT, lambda: click_button('8')), 
    ('9', 2, 2, 1, BG_DEFAULT, lambda: click_button('9')), 
    ('*', 2, 3, 1, BG_OPERATOR, lambda: click_button('*')),
    ('4', 3, 0, 1, BG_DEFAULT, lambda: click_button('4')), 
    ('5', 3, 1, 1, BG_DEFAULT, lambda: click_button('5')), 
    ('6', 3, 2, 1, BG_DEFAULT, lambda: click_button('6')), 
    ('-', 3, 3, 1, BG_OPERATOR, lambda: click_button('-')),
    ('1', 4, 0, 1, BG_DEFAULT, lambda: click_button('1')), 
    ('2', 4, 1, 1, BG_DEFAULT, lambda: click_button('2')), 
    ('3', 4, 2, 1, BG_DEFAULT, lambda: click_button('3')), 
    ('+', 4, 3, 1, BG_OPERATOR, lambda: click_button('+')),
    ('0', 5, 0, 2, BG_DEFAULT, lambda: click_button('0')),
    ('.', 5, 2, 1, BG_DEFAULT, lambda: click_button('.')), 
    ('=', 5, 3, 1, BG_EQUALS, calculate),
]
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

for (text, row, col, colspan, bg_color, command) in buttons_data:
    btn = tk.Button(
        root, 
        text=text, 
        font=FONT_STYLE, 
        bg=bg_color, 
        fg=FG_DEFAULT, 
        relief="flat",
        command=command
    )
    btn.grid(
        row=row, 
        column=col, 
        columnspan=colspan, 
        padx=5, 
        pady=5, 
        sticky="nsew"
    )
    if text == 'C':
        btn.grid(columnspan=3) 
root.mainloop()