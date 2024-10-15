def is_armstrong(n):
    num_digits = 0
    number = n

    while number > 0:
        num_digits += 1
        number //= 10
    
    armstrong_sum = 0
    number = n 
    while number > 0:
        digit = number % 10
        armstrong_sum += digit ** num_digits
        number //= 10
    
    return armstrong_sum == n
n=int(input())
print(is_armstrong(n))
