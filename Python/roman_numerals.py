"""
Roman numeral utilities

This module provides two high-level functions:
- int_to_roman(number: int) -> str
- roman_to_int(numeral: str) -> int

Both functions validate inputs and raise ValueError for invalid cases.

Run this file directly to use a simple CLI for conversions.
"""

from typing import Dict


_INT_TO_ROMAN_PAIRS: tuple[tuple[int, str], ...] = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)

_ROMAN_TO_INT_MAP: Dict[str, int] = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def int_to_roman(number: int) -> str:
    """Convert an integer to a Roman numeral.

    Supports values from 1 to 3999 inclusive.
    Raises ValueError for out-of-range or non-integer inputs.
    """
    if not isinstance(number, int):
        raise ValueError("number must be an integer")
    if number <= 0 or number >= 4000:
        raise ValueError("number must be between 1 and 3999 inclusive")

    result_parts: list[str] = []
    remaining = number
    for value, symbol in _INT_TO_ROMAN_PAIRS:
        if remaining == 0:
            break
        count, remaining = divmod(remaining, value)
        if count:
            result_parts.append(symbol * count)
    return "".join(result_parts)


def roman_to_int(numeral: str) -> int:
    """Convert a Roman numeral to an integer.

    Validates standard subtractive notation and character set. Case-insensitive.
    Raises ValueError for invalid strings.
    """
    if not isinstance(numeral, str) or not numeral.strip():
        raise ValueError("numeral must be a non-empty string")

    s = numeral.strip().upper()
    total = 0
    i = 0

    while i < len(s):
        current_char = s[i]
        if current_char not in _ROMAN_TO_INT_MAP:
            raise ValueError(f"invalid Roman numeral character: {current_char}")

        current_value = _ROMAN_TO_INT_MAP[current_char]

        if i + 1 < len(s):
            next_char = s[i + 1]
            if next_char not in _ROMAN_TO_INT_MAP:
                raise ValueError(f"invalid Roman numeral character: {next_char}")
            next_value = _ROMAN_TO_INT_MAP[next_char]

            if current_value < next_value:
                # Validate allowed subtractive pairs
                if current_char == "I" and next_char not in ("V", "X"):
                    raise ValueError("invalid subtractive pair: I can precede V or X only")
                if current_char == "X" and next_char not in ("L", "C"):
                    raise ValueError("invalid subtractive pair: X can precede L or C only")
                if current_char == "C" and next_char not in ("D", "M"):
                    raise ValueError("invalid subtractive pair: C can precede D or M only")

                total += next_value - current_value
                i += 2
                continue

        total += current_value
        i += 1

    # Convert back to Roman to ensure canonical form matches input when normalized
    # This guards against sequences like "IM" which might numerically process but are invalid
    try:
        canonical = int_to_roman(total)
    except ValueError:
        raise ValueError("resulting value is out of supported range")

    if canonical != s:
        # Accept non-canonical but equivalent forms only if they strictly match canonical when uppercased
        # e.g., "xvii" is allowed because upper() makes it canonical; "iiiii" is rejected
        # since canonical for 5 is "V"
        raise ValueError("invalid or non-canonical Roman numeral sequence")

    return total


def _print_examples() -> None:
    examples = [1, 4, 9, 29, 44, 58, 94, 145, 3999]
    print("Examples (int -> roman -> int):")
    for n in examples:
        r = int_to_roman(n)
        back = roman_to_int(r)
        print(f"  {n} -> {r} -> {back}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert between Roman numerals and integers.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--to-roman", type=int, dest="to_roman", help="Convert integer to Roman numeral")
    group.add_argument("--to-int", type=str, dest="to_int", help="Convert Roman numeral to integer")
    parser.add_argument("--examples", action="store_true", help="Show example conversions")

    args = parser.parse_args()

    if args.examples:
        _print_examples()

    if args.to_roman is not None:
        print(int_to_roman(args.to_roman))
    elif args.to_int is not None:
        print(roman_to_int(args.to_int))


