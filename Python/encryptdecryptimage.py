import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
def swap_pixels(image):
    pixels = image.load()
    width, height = image.size
    for i in range(0, width, 2):
        for j in range(0, height, 2):
            if i+1 < width and j+1 < height:
                # Swap pixel values
                pixels[i, j], pixels[i+1, j+1] = pixels[i+1, j+1], pixels[i, j]
    return image
def apply_math_operation(image, key):
    pixels = image.load()
    width, height = image.size
    for i in range(width):
        for j in range(height):
            pixel = pixels[i, j]
            if len(pixel) == 4:
                r, g, b, a = pixel
                pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256, a)  # Keep alpha unchanged
            else:  # For RGB images
                r, g, b = pixel
                pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    return image
def encrypt_image():
    global img, encrypted_img
    if img:
        encrypted_img = img.copy()
        encrypted_img = swap_pixels(encrypted_img)
        encrypted_img = apply_math_operation(encrypted_img, key=15)  # Simple key for manipulation
        display_image(encrypted_img)
def decrypt_image():
    global img, encrypted_img
    if encrypted_img:
        decrypted_img = encrypted_img.copy()
        decrypted_img = apply_math_operation(decrypted_img, key=-15)  # Reverse key
        decrypted_img = swap_pixels(decrypted_img)  # Apply the same swap
        display_image(decrypted_img)
def load_image():
    global img
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img = Image.open(file_path)
        display_image(img)
def display_image(image):
    img_display = ImageTk.PhotoImage(image.resize((300, 300)))  # Resize for display
    panel.config(image=img_display)
    panel.image = img_display
root = tk.Tk()
root.title("Image Encryption Tool")
img = None
encrypted_img = None
load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.grid(row=0, column=0, padx=10, pady=10)

encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt_image)
encrypt_button.grid(row=1, column=0, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt_image)
decrypt_button.grid(row=2, column=0, padx=10, pady=10)
panel = tk.Label(root)
panel.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

root.mainloop()