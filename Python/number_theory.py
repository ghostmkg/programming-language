"""
Number Theory Algorithms
=========================

Prime numbers, GCD/LCM, modular arithmetic, and other
number theory algorithms for competitive programming.

Author: Hacktoberfest 2025 Contributor
"""

import math
from typing import List, Tuple


class NumberTheory:
    """Collection of number theory algorithms"""
    
    @staticmethod
    def sieve_of_eratosthenes(n: int) -> List[int]:
        """
        Find all primes up to n using Sieve of Eratosthenes
        
        Time: O(n log log n)
        Space: O(n)
        """
        if n < 2:
            return []
        
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        
        return [i for i in range(n + 1) if is_prime[i]]
    
    @staticmethod
    def is_prime(n: int) -> bool:
        """
        Check if number is prime
        
        Time: O(sqrt(n))
        """
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        
        return True
    
    @staticmethod
    def prime_factorization(n: int) -> List[Tuple[int, int]]:
        """
        Find prime factorization of n
        
        Time: O(sqrt(n))
        Returns: List of (prime, power) tuples
        """
        factors = []
        
        # Handle 2 separately
        if n % 2 == 0:
            count = 0
            while n % 2 == 0:
                count += 1
                n //= 2
            factors.append((2, count))
        
        # Check odd numbers
        i = 3
        while i * i <= n:
            if n % i == 0:
                count = 0
                while n % i == 0:
                    count += 1
                    n //= i
                factors.append((i, count))
            i += 2
        
        if n > 1:
            factors.append((n, 1))
        
        return factors
    
    @staticmethod
    def gcd(a: int, b: int) -> int:
        """
        Greatest Common Divisor using Euclidean algorithm
        
        Time: O(log(min(a, b)))
        """
        while b:
            a, b = b, a % b
        return a
    
    @staticmethod
    def lcm(a: int, b: int) -> int:
        """
        Least Common Multiple
        
        Time: O(log(min(a, b)))
        """
        return (a * b) // NumberTheory.gcd(a, b)
    
    @staticmethod
    def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
        """
        Extended Euclidean Algorithm
        Returns: (gcd, x, y) where ax + by = gcd(a, b)
        
        Time: O(log(min(a, b)))
        """
        if b == 0:
            return a, 1, 0
        
        gcd, x1, y1 = NumberTheory.extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        
        return gcd, x, y
    
    @staticmethod
    def mod_inverse(a: int, m: int) -> int:
        """
        Modular multiplicative inverse of a under modulo m
        
        Time: O(log m)
        """
        gcd, x, _ = NumberTheory.extended_gcd(a, m)
        
        if gcd != 1:
            return -1  # Inverse doesn't exist
        
        return (x % m + m) % m
    
    @staticmethod
    def mod_power(base: int, exp: int, mod: int) -> int:
        """
        Fast modular exponentiation: (base^exp) % mod
        
        Time: O(log exp)
        """
        result = 1
        base = base % mod
        
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            
            exp = exp >> 1
            base = (base * base) % mod
        
        return result
    
    @staticmethod
    def chinese_remainder_theorem(remainders: List[int], moduli: List[int]) -> int:
        """
        Chinese Remainder Theorem
        
        Time: O(n * log(max(moduli)))
        """
        total = 0
        prod = 1
        
        for m in moduli:
            prod *= m
        
        for r, m in zip(remainders, moduli):
            p = prod // m
            total += r * NumberTheory.mod_inverse(p, m) * p
        
        return total % prod
    
    @staticmethod
    def euler_totient(n: int) -> int:
        """
        Euler's Totient Function: count of numbers <= n coprime to n
        
        Time: O(sqrt(n))
        """
        result = n
        p = 2
        
        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n //= p
                result -= result // p
            p += 1
        
        if n > 1:
            result -= result // n
        
        return result
    
    @staticmethod
    def count_divisors(n: int) -> int:
        """
        Count number of divisors
        
        Time: O(sqrt(n))
        """
        count = 0
        
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                if n // i == i:
                    count += 1
                else:
                    count += 2
        
        return count
    
    @staticmethod
    def sum_of_divisors(n: int) -> int:
        """
        Sum of all divisors
        
        Time: O(sqrt(n))
        """
        total = 0
        
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                total += i
                if i != n // i:
                    total += n // i
        
        return total
    
    @staticmethod
    def fibonacci_matrix(n: int) -> int:
        """
        Fibonacci using matrix exponentiation
        
        Time: O(log n)
        """
        def matrix_multiply(a, b):
            return [
                [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
                [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
            ]
        
        def matrix_power(mat, n):
            if n == 1:
                return mat
            
            if n % 2 == 0:
                half = matrix_power(mat, n // 2)
                return matrix_multiply(half, half)
            else:
                return matrix_multiply(mat, matrix_power(mat, n - 1))
        
        if n <= 1:
            return n
        
        base = [[1, 1], [1, 0]]
        result = matrix_power(base, n)
        
        return result[0][1]
    
    @staticmethod
    def is_perfect_square(n: int) -> bool:
        """
        Check if number is perfect square
        
        Time: O(log n)
        """
        if n < 0:
            return False
        
        sqrt = int(math.sqrt(n))
        return sqrt * sqrt == n
    
    @staticmethod
    def catalan_number(n: int) -> int:
        """
        Calculate nth Catalan number
        
        Time: O(n)
        """
        if n <= 1:
            return 1
        
        catalan = [0] * (n + 1)
        catalan[0] = catalan[1] = 1
        
        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - 1 - j]
        
        return catalan[n]


# Demonstration
def demonstrate_number_theory():
    print("=" * 70)
    print("NUMBER THEORY ALGORITHMS DEMONSTRATION")
    print("=" * 70)
    
    nt = NumberTheory()
    
    # Sieve of Eratosthenes
    print("\n1. SIEVE OF ERATOSTHENES")
    primes = nt.sieve_of_eratosthenes(30)
    print(f"   Primes up to 30: {primes}")
    
    # Prime Check
    print("\n2. PRIME CHECK")
    print(f"   Is 17 prime? {nt.is_prime(17)}")
    print(f"   Is 18 prime? {nt.is_prime(18)}")
    
    # Prime Factorization
    print("\n3. PRIME FACTORIZATION")
    n = 60
    factors = nt.prime_factorization(n)
    print(f"   {n} = {' × '.join([f'{p}^{e}' if e > 1 else str(p) for p, e in factors])}")
    
    # GCD and LCM
    print("\n4. GCD AND LCM")
    a, b = 48, 18
    print(f"   GCD({a}, {b}) = {nt.gcd(a, b)}")
    print(f"   LCM({a}, {b}) = {nt.lcm(a, b)}")
    
    # Modular Exponentiation
    print("\n5. MODULAR EXPONENTIATION")
    print(f"   (2^10) mod 1000 = {nt.mod_power(2, 10, 1000)}")
    
    # Modular Inverse
    print("\n6. MODULAR INVERSE")
    a, m = 3, 11
    inv = nt.mod_inverse(a, m)
    print(f"   Inverse of {a} mod {m} = {inv}")
    print(f"   Verification: ({a} × {inv}) mod {m} = {(a * inv) % m}")
    
    # Euler's Totient
    print("\n7. EULER'S TOTIENT FUNCTION")
    n = 12
    print(f"   φ({n}) = {nt.euler_totient(n)}")
    
    # Divisors
    print("\n8. DIVISORS")
    n = 28
    print(f"   Number of divisors of {n}: {nt.count_divisors(n)}")
    print(f"   Sum of divisors of {n}: {nt.sum_of_divisors(n)}")
    
    # Fibonacci (Matrix)
    print("\n9. FIBONACCI (FAST)")
    print(f"   Fib(10) = {nt.fibonacci_matrix(10)}")
    print(f"   Fib(20) = {nt.fibonacci_matrix(20)}")
    
    # Catalan Numbers
    print("\n10. CATALAN NUMBERS")
    for i in range(6):
        print(f"   C({i}) = {nt.catalan_number(i)}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    demonstrate_number_theory()
