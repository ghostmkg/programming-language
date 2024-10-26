from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("filekey.key", "wb") as filekey:
        filekey.write(key)

def load_key():
    return open("filekey.key", "rb").read()

def encrypt_file(filename, key):
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = Fernet(key).encrypt(file_data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename, key):
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = Fernet(key).decrypt(encrypted_data)
    with open(filename.replace(".enc", ""), "wb") as file:
        file.write(decrypted_data)
