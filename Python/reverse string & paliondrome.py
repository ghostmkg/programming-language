def reversestring(s):
    return s[::-1]


def ispalindrome(s):
    rev = reversestring(s)
    print("Reversed String is:", rev)
    if s == rev:
        return True
    else:
        return False


def main():
    s = input("Enter a string:")
    ans = ispalindrome(s)
    if ans:
        print("Yes, It's a Palindrome")
    else:
        print("No, It's not a Palindrome")


if __name__ == "__main__":
    main()
