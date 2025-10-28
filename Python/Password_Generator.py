import random
import string

def generate_password(length=12, use_special=True):
    """Generate a secure random password."""
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation if use_special else ""
    all_chars = letters + digits + specials

    if length < 4:
        print("Password length too short, minimum is 4.")
        return ""

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation) if use_special else random.choice(string.ascii_letters)
    ]

    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return "".join(password)

def main():
    print("===== Password Generator =====")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
    except ValueError:
        print("Invalid input, using default length 12.")
        length = 12

    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    pwd = generate_password(length, use_special)
    if pwd:
        print(f"\nGenerated Password: {pwd}\n")

if __name__ == "__main__":
    main()
