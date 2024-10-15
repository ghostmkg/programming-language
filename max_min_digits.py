def min_max_digits(n):

    digits = [int(digit) for digit in str(n)]
        
    min_digit = min(digits)
    max_digit = max(digits)
    return min_digit,max_digit
n=int(input())
print(min_max_digits(n))
