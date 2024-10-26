# Fibonacci_Sequence.py

def fibonacci(n):
    """Generate the Fibonacci sequence up to the n-th number."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of Fibonacci terms to generate: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            fib_sequence = fibonacci(n)
            print(f"The first {n} terms of the Fibonacci sequence are: {fib_sequence}")
    except ValueError:
        print("Please enter a valid integer.")
