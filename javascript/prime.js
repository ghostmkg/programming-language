function isPrime(number) {
    if (number <= 1) return false; // Numbers less than 2 are not prime
    if (number <= 3) return true;  // 2 and 3 are prime numbers
    if (number % 2 === 0 || number % 3 === 0) return false; // Eliminate multiples of 2 and 3
  
    // Check for factors from 5 up to the square root of the number
    for (let i = 5; i * i <= number; i += 6) {
      if (number % i === 0 || number % (i + 2) === 0) return false;
    }
  
    return true;
  }
  
  // Example usage
  console.log(isPrime(11));  
  console.log(isPrime(25));  
  console.log(isPrime(37));