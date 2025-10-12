def factorial(n: int) -> int:
    """
    Returns the factorial of n using recursion.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return 1 if n == 0 else n * factorial(n - 1)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Factorial:", factorial(num))
