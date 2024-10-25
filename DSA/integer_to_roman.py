def integer_to_roman(num: int) -> str:
    # Define mappings of integer values to Roman numerals
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_numeral = ""
    
    # Iterate through each value-symbol pair
    for i in range(len(val)):
        while num >= val[i]:
            roman_numeral += syms[i]
            num -= val[i]

    return roman_numeral

# Example usage:
print(integer_to_roman(3))      # "III"
print(integer_to_roman(4))      # "IV"
print(integer_to_roman(9))      # "IX"
print(integer_to_roman(58))     # "LVIII"
print(integer_to_roman(1994))    # "MCMXCIV"
