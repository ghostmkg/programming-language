def are_anagrams(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams.
    """
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())


if __name__ == "__main__":
    s1 = input("Enter first word: ")
    s2 = input("Enter second word: ")
    print("Anagrams:", are_anagrams(s1, s2))
