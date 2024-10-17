import sys
import time,customtkinter as tk
from tkinter import messagebox

Time=0
def Healthy():
    def hehe():
        def start_timer():
            if not timer_running.get():
                timer_running.set(True)
                update_timer()

        def update_timer():
            if remaining_time.get() > 0 and timer_running.get():
                timer_label.configure(text=str(remaining_time.get()))
                remaining_time.set(remaining_time.get() - 1)
                root.after(1000, update_timer)
            else:
                timer_running.set(False)
                remaining_time.set(20)
                timer_label.configure(text="20")
                root.destroy()
                messagebox.showinfo("Timer Complete", f"After {Time} min you will be reminded again")

        def Bye():
            sys.exit()
        timee=Time*60 #####################
        while True:
            time.sleep(timee)
            root = tk.CTk()

            root.resizable(False,False)


            root.title("Healthy eyes")
            timer_running = tk.BooleanVar()
            remaining_time = tk.IntVar(value=20)
            tk.CTkLabel(root,text= "You need to look 20 meters away from the screen\nwhile the timer ends\n\nYou can also blink your eyes constantly\nwhile the timer ends",font=("Helvetica", 20)).pack(padx=20,pady=10)
            timer_label = tk.CTkLabel(root, text="20", font=("Helvetica", 248))
            timer_label.pack()
            tk.CTkLabel(root,text="To Start the timer hit Start",font=("Helvetica", 20)).pack(pady=10)
            start_button = tk.CTkButton(root, text="Start", command=start_timer).pack()
            tk.CTkLabel(root,text="To close the app hit exit.",font=("Helvetica", 20)).pack(pady=10)
            close_button = tk.CTkButton(root,text="Exit",command=Bye).pack(pady=10)
            root.mainloop()

    def com1():
        try:
            global Time
            Time = int(Time_entry.get())
            if not Time:
                raise ValueError("Time is empty")
            time_value = int(Time)
            if not (1 <= time_value <= 60):
                raise ValueError("Please enter time in the range 1-60")
            timeroot.destroy()
            messagebox.showinfo("Timer",f"Your timer is started for {Time} minutes\nYou will be reminded after every {Time} min")
            hehe()
        except ValueError as e:
            messagebox.showerror("Error", str(e))



    timeroot=tk.CTk()

    timeroot.resizable(False,False)
    screen_width = timeroot.winfo_screenwidth()
    screen_height = timeroot.winfo_screenheight()
    x_coordinate = (screen_width - timeroot.winfo_reqwidth()) / 2
    y_coordinate = (screen_height - timeroot.winfo_reqheight()) / 2
    timeroot.geometry("+%d+%d" % (x_coordinate, y_coordinate))

    timeroot.title("Healthy eyes")
    tk.CTkLabel(timeroot,text="Enter the time you want to get remainders\n20 min is recommended").grid(padx=20,pady=10)
    Time_entry = tk.CTkEntry(timeroot,width=100)
    Time_entry.grid(row=1,column=0,pady=10,padx=50)
    tk.CTkLabel(timeroot,text="min").grid(column=0,row=1,sticky='E',padx=60)
    tk.CTkButton(timeroot,text="ok",command=com1).grid()
    timeroot.mainloop()
  Healthy()
