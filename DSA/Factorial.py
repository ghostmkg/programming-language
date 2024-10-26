# Factorial.py

def factorial(n):
    """Calculate the factorial of a number recursively."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    # Example usage
    try:
        number = int(input("Enter a non-negative integer: "))
        result = factorial(number)
        print(f"The factorial of {number} is {result}.")
    except ValueError as e:
        print(e)
