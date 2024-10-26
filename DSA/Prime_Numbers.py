# Prime_Numbers.py

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(limit):
    """Find all prime numbers up to a specified limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    try:
        limit = int(input("Enter a positive integer limit: "))
        if limit < 2:
            print("There are no prime numbers less than 2.")
        else:
            primes = find_primes(limit)
            print(f"Prime numbers up to {limit}: {primes}")
    except ValueError:
        print("Please enter a valid integer.")
