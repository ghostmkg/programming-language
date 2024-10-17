import customtkinter as tk,tkinter as tkin,datetime,time # type: ignore
from tkinter import ttk,messagebox
from tkcalendar import Calendar # type: ignore

def block():
    TIM = "23:59"
    def Date_selection(): # A calendar UI for selecting date
        def print_sel():
            date_data = cal.selection_get()
            end_time_entry.delete(0, tk.END)
            end_time_entry.insert(0, date_data)
            calroot.destroy()

        calroot = tkin.Tk()
        s = ttk.Style(calroot)
        s.theme_use('clam')
        current_date = datetime.datetime.now()
        cal = Calendar(calroot, font="Arial 14", selectmode='day', cursor="hand1", year=current_date.year, month=current_date.month, day=current_date.day)
        cal.pack(fill="both", expand=True)
        ttk.Button(calroot, text="Select Date", command=print_sel).pack()
        calroot.mainloop()

    def time_selector(): #UI for selecting time
        def update_time():
            selected_hour = hour_spinbox.get()
            selected_minute = minute_spinbox.get()
            selected_time.set(f"Selected Time: {selected_hour.zfill(2)}:{selected_minute.zfill(2)}")

        def save_and_close():
            selected_hour = hour_spinbox.get()
            selected_minute = minute_spinbox.get()
            if 0 <= int(selected_hour) <= 23 and 0 <= int(selected_minute) <= 59:
                global TIM
                TIM = f"{selected_hour.zfill(2)}:{selected_minute.zfill(2)}"
                time_label.configure(text=f"Time: {TIM}"+':59')
                timeroot.destroy()
            else:
                messagebox.showerror("Invalid Time", "Please enter a valid time (00:00 - 23:59)")
        timeroot = tkin.Tk()
        timeroot.title("Time Selector")
        hour_label = ttk.Label(timeroot, text="Hour:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        hour_spinbox = ttk.Spinbox(timeroot, from_=0, to=23, wrap=True, width=5, command=update_time)
        hour_spinbox.grid(row=0, column=1, padx=10, pady=10)
        minute_label = ttk.Label(timeroot, text="Minute:").grid(row=0, column=2, padx=10, pady=10, sticky="e")
        minute_spinbox = ttk.Spinbox(timeroot, from_=0, to=59, wrap=True, width=5, command=update_time)
        minute_spinbox.grid(row=0, column=3, padx=10, pady=10)
        selected_time = tk.StringVar()
        selected_time.set(f"Selected Time: {TIM}")
        time_labe = ttk.Label(timeroot, textvariable=selected_time).grid(row=1, column=0, columnspan=4, pady=10)
        ok_button = ttk.Button(timeroot, text="OK", command=save_and_close).grid(row=2, column=0, columnspan=4, pady=10)
        # Set default time
        default_hour, default_minute= TIM.split(":")
        hour_spinbox.delete(0, tk.END)
        hour_spinbox.insert(0, default_hour)
        minute_spinbox.delete(0, tk.END)
        minute_spinbox.insert(0, default_minute)
        timeroot.mainloop()

    def block_website():
        site_to_block = website_entry.get()
        end_time_input = end_time_entry.get()
        end_tim = end_time_input + ' ' + TIM + ':59'
        end_time = datetime.datetime.strptime(end_tim, "%Y-%m-%d %H:%M:%S")
        host_path = r"C:\Windows\System32\drivers\etc\hosts"
        redirect = "127.0.0.1"
        # Block the website until the specified end time
        while datetime.datetime.now() < end_time:
            with open(host_path, "r+") as host_file:
                content = host_file.read()
                if site_to_block not in content:
                    host_file.write(redirect + ' ' + site_to_block + '\n')
            time.sleep(5)
            messagebox.showinfo("Website Blocker","Website blocked sucessfully")
            root.destroy()
        # Unblock the website after the specified end time
        while True:
            if datetime.datetime.now() >= end_time:
                with open(host_path, "r+") as host_file:
                    content = host_file.readlines()
                    host_file.seek(0)
                    for line in content:
                        if site_to_block not in line:
                            host_file.write(line)
                    host_file.truncate()
                break
        

    root = tk.CTk()
    root.resizable(False,False)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - root.winfo_reqwidth()) / 2
    y_coordinate = (screen_height - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x_coordinate, y_coordinate))

    root.title("Website Blocker")

    tk.CTkLabel(root,font=("Arial",15, "bold"), text="Enter the website to block (e.g., www.facebook.com):").grid(padx=30,pady=0)
    website_entry = tk.CTkEntry(root,width=250)
    website_entry.grid(padx=20,pady=20)
    tk.CTkLabel(root, text="Select the end time for blocking:",font=("Arial", 15, "bold")).grid(sticky='W',padx=20)
    end_time_entry = tk.CTkEntry(root)
    end_time_entry.grid(sticky='E',padx=20,row=2,column=0,pady=0)

    tk.CTkButton(root, text="Select End Date", command=Date_selection,font=("Arial", 15, "bold")).grid(padx=20,sticky='E',pady=10)
    time_label=tk.CTkLabel(root,text="Time:23:59:59",font=("Arial", 15, "bold"))
    time_label.grid(sticky='W',padx=20,row=3)
    tk.CTkButton(root, text="Select time",command=time_selector,width=30,font=("Arial", 15, "bold")).grid(row=3)
    tk.CTkButton(root, text="Block Website", command=block_website,font=("Arial", 15, "bold")).grid(pady=10)

    root.mainloop()
