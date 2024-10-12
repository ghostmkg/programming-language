function isPrime(num) {
  if (num <= 1) return false; // Numbers less than 2 are not prime
  if (num === 2) return true; // 2 is the only even prime number
  if (num % 2 === 0) return false; // Eliminate other even numbers
  
  for (let i = 3; i <= Math.sqrt(num); i += 2) {
    if (num % i === 0) return false; // If divisible by any odd number, it's not prime
  }
  
  return true;
}

// Example usage
console.log(isPrime(7));  // true
console.log(isPrime(10)); // false
