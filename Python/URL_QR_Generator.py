from tkinter import *
from tkinter.messagebox import *
from qrcode import *
from PIL import Image, ImageTk

root = Tk()
root.title("QR Code Generator")
root.geometry("500x600+200+20")

# Define colors
bg_color = "#DAE6F0"  # Light blue background
label_color = "#333333"  # Dark gray for labels
entry_color = "#ffffff"  # White for entry fields
button_color = "#4CAF50"  # Green for buttons
button_text_color = "#ffffff"  # White text for buttons

# Define fonts
heading_font = ("Arial", 30, "bold")
label_font = ("Verdana", 15)  # Smaller font size, changed font style
button_font = ("Arial", 20, "bold")

# Function to generate QR code
def generate_qr():
    url = ent_url.get()
    if url == "":
        showerror("Error", "URL is empty")
        ent_url.focus()
        return
    
    # Generate QR code
    img = make(url)
    img.save("qr2.png")
    img = Image.open("qr2.png")
    new_size = (400, 400)
    resized_img = img.resize(new_size)
    resized_img.save("qr2.png")
    img = Image.open("qr2.png")
    imgtk = ImageTk.PhotoImage(image=img)
    lab_qr.configure(image=imgtk)
    lab_qr.photo = imgtk

# Configure root window
root.configure(bg=bg_color)

# Labels, Entry, Button, and QR Code display
lab_url = Label(root, text="Enter URL", font=heading_font, fg=label_color, bg=bg_color)
ent_url = Entry(root, font=label_font, bg=entry_color)
btn_generate = Button(root, text="Generate QR Code", font=button_font, bg=button_color, fg=button_text_color, command=generate_qr)
lab_qr = Label(root, font=label_font, bg=bg_color)

# Packing widgets
lab_url.pack(pady=10)
ent_url.pack(pady=10)
btn_generate.pack(pady=10)
lab_qr.pack(pady=10)

root.mainloop()
