import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''
    
    # Combine all selected characters
    all_chars = letters + digits + symbols
    if not all_chars:
        raise ValueError("No character sets selected for password generation.")
    
    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Example usage
print("Generated password:", generate_password(length=16))