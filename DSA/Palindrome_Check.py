def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Example usage
if __name__ == "__main__":
    test_strings = [
        "A man, a plan, a canal, Panama!",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon",
        "Hello, World!"
    ]

    for string in test_strings:
        if is_palindrome(string):
            print(f'"{string}" is a palindrome.')
        else:
            print(f'"{string}" is not a palindrome.')
