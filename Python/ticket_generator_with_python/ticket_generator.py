import qrcode
from PIL import Image

def generate_qr_code(text, qr_size=50):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img = img.resize((qr_size, qr_size))  
    return img.convert('RGBA') 


def add_qr_to_image(base_image_path, qr_image, qr_text,position=(0, 0)):
    
    base_image = Image.open(base_image_path).convert('RGBA') 
    base_image.paste(qr_image, position, qr_image)  
    base_image.save('ticket_with_QR_Code.png',sep="")

text_input = input("Enter the text: ")
qr_text = text_input
qr_size = 320
qr_code = generate_qr_code(qr_text, qr_size)

base_image_path = 'img1.png' 
add_qr_to_image(base_image_path, qr_code, qr_text,position=(900, 200)) 