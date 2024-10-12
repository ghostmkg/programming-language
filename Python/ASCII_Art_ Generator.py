from PIL import Image

# ASCII characters used to represent pixel intensity
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# Resize the image to fit within terminal size
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert('L')
    return grayscale_image

# Map each pixel to an ASCII character
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

# Main function to convert image to ASCII
def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file: {e}")
        return

    image = resize_image(image, new_width)
    image = grayify(image)
    
    ascii_str = pixels_to_ascii(image)
    
    # Format the string into lines of the correct width
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[i:i + img_width] for i in range(0, ascii_str_len, img_width)])
    
    return ascii_img

# Run the program with an example image
if __name__ == "__main__":
    path = input("Enter the image path: ")
    ascii_art = image_to_ascii(path)
    print(ascii_art)

    # Optionally save to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_art)
