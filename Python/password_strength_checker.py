# password_strength_checker.py
# CLI Password Strength Checker with colors and masked input

import re
from getpass import getpass

# Terminal colors
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Include at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character (!@#$%^&*...).")

    return score, suggestions

def main():
    print(f"{Colors.BLUE}=== Password Strength Checker ==={Colors.RESET}")
    password = getpass("Enter your password: ")  # Masked input
    score, suggestions = check_password_strength(password)

    print(f"\nPassword Strength Score: {score}/5")
    if score == 5:
        print(f"{Colors.GREEN}Great! Your password is strong.{Colors.RESET}")
    elif score >= 3:
        print(f"{Colors.YELLOW}Medium strength. Improve it with the suggestions below:{Colors.RESET}")
    else:
        print(f"{Colors.RED}Weak password. Follow these suggestions:{Colors.RESET}")

    for s in suggestions:
        print(f"- {s}")

if __name__ == "__main__":
    main()

