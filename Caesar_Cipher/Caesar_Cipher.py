class CaesarCipher:
    def __init__(self, shift=3):
        self.shift = shift

    def encrypt(self, text: str) -> str:
        result = ""
        for char in text:
            if char.isalpha():
                base = 'A' if char.isupper() else 'a'
                result += chr((ord(char) - ord(base) + self.shift) % 26 + ord(base))
            else:
                result += char
        return result

    def decrypt(self, text: str) -> str:
        result = ""
        for char in text:
            if char.isalpha():
                base = 'A' if char.isupper() else 'a'
                result += chr((ord(char) - ord(base) - self.shift) % 26 + ord(base))
            else:
                result += char
        return result

def main():
    print("---Caesar Cipher---")
    shift = int(input("Enter the shift value needed(default 3): ") or 3)
    cipher = CaesarCipher(shift)

    while True:
        print("\n--- Menu ---")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter choice(1,2,3): ").strip()

        if choice == "1":
            text = input("Enter the text to encrypt: ")
            encrypted = cipher.encrypt(text)
            print("The Encrypted Text is: ", encrypted)

        elif choice == "2":
            text = input("Enter the text to decrypt: ")
            decrypted = cipher.decrypt(text)
            print("The Decrypted Text is: ", decrypted)

        elif choice == "3":
            print("Thank you for chosing CaesarCipher!")
            break

        else:
            print("Invalid choice. Please, Try again.")

if __name__ == "__main__":
    main()