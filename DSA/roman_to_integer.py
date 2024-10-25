def roman_to_integer(s: str) -> int:
    # Mapping of Roman numerals to integers
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Iterate over the Roman numeral from right to left
    for char in reversed(s):
        current_value = roman_map[char]

        # If the current value is less than the previous value, subtract it
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        # Update the previous value
        prev_value = current_value

    return total

# Example usage:
print(roman_to_integer("III"))     # 3
print(roman_to_integer("IV"))      # 4
print(roman_to_integer("IX"))      # 9
print(roman_to_integer("LVIII"))   # 58
print(roman_to_integer("MCMXCIV")) # 1994
