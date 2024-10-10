# prime_generator.py

# Function to check if a number is prime
def is_prime(n):
    """Check if a number is prime."""
    # A prime number is greater than 1
    if n <= 1:
        return False
    # Check divisibility from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:  # If divisible, n is not prime
            return False
    return True  # If no divisors, n is prime

# Function to generate all primes up to a limit
def generate_primes(limit):
    """Generate all prime numbers up to a given limit."""
    primes = []  # List to store prime numbers
    # Loop through each number from 2 to the limit
    for num in range(2, limit + 1):
        # Use the is_prime function to check if num is prime
        if is_prime(num):
            primes.append(num)  # Add prime numbers to the list
    return primes  # Return the list of prime numbers

# Main function to run the program
if __name__ == "__main__":
    # Ask the user to input the upper limit for prime generation
    limit = int(input("Enter the upper limit to generate prime numbers: "))
    # Call the function to generate prime numbers
    primes = generate_primes(limit)
    # Print the list of prime numbers
    print(f"Prime numbers up to {limit}: {primes}")
