"""
Palindrome utilities with a simple CLI.

Functions:
- is_palindrome(text: str, ignore_case: bool = True, ignore_non_alnum: bool = True) -> bool
- longest_palindromic_substring(text: str) -> str

Run this file directly to access a small CLI for quick checks.
"""

from typing import Tuple


def _normalize(text: str, ignore_case: bool, ignore_non_alnum: bool) -> str:
    if ignore_case:
        text = text.lower()
    if ignore_non_alnum:
        text = "".join(ch for ch in text if ch.isalnum())
    return text


def is_palindrome(text: str, ignore_case: bool = True, ignore_non_alnum: bool = True) -> bool:
    """Return True if text is a palindrome under the chosen normalization options."""
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    normalized = _normalize(text, ignore_case=ignore_case, ignore_non_alnum=ignore_non_alnum)
    return normalized == normalized[::-1]


def longest_palindromic_substring(text: str) -> str:
    """Return the longest palindromic substring using expand-around-center.

    For ties, the first occurring longest substring is returned.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    if not text:
        return ""

    def expand(left: int, right: int) -> Tuple[int, int]:
        while left >= 0 and right < len(text) and text[left] == text[right]:
            left -= 1
            right += 1
        return left + 1, right  # inclusive start, exclusive end

    best_start, best_end = 0, 1
    for center in range(len(text)):
        # Odd-length palindrome
        s1, e1 = expand(center, center)
        if e1 - s1 > best_end - best_start:
            best_start, best_end = s1, e1
        # Even-length palindrome
        if center + 1 < len(text):
            s2, e2 = expand(center, center + 1)
            if e2 - s2 > best_end - best_start:
                best_start, best_end = s2, e2

    return text[best_start:best_end]


def _print_examples() -> None:
    cases = [
        "racecar",
        "A man, a plan, a canal: Panama!",
        "hello",
        "forgeeksskeegfor",
        "abba",
        "",
    ]
    print("Examples:")
    for c in cases:
        print(f"  '{c}' -> is_palindrome: {is_palindrome(c)}; LPS: '{longest_palindromic_substring(c)}'")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Palindrome utilities: check or find longest palindromic substring.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_check = sub.add_parser("check", help="Check if a string is a palindrome")
    p_check.add_argument("text", type=str, help="Input text")
    p_check.add_argument("--case-sensitive", action="store_true", help="Make check case-sensitive")
    p_check.add_argument("--keep-non-alnum", action="store_true", help="Do not strip non-alphanumeric characters")

    p_lps = sub.add_parser("lps", help="Find the longest palindromic substring")
    p_lps.add_argument("text", type=str, help="Input text")

    parser.add_argument("--examples", action="store_true", help="Show example outputs")

    args = parser.parse_args()

    if args.examples:
        _print_examples()

    if args.command == "check":
        ignore_case = not args.case_sensitive
        ignore_non_alnum = not args.keep_non_alnum
        print(is_palindrome(args.text, ignore_case=ignore_case, ignore_non_alnum=ignore_non_alnum))
    elif args.command == "lps":
        print(longest_palindromic_substring(args.text))


