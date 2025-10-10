function atoi(str) {
  let i = 0;
  let sign = 1;
  let result = 0;

  // Skip leading whitespace
  while (i < str.length && str[i] === ' ') i++;

  // Check for sign
  if (str[i] === '+' || str[i] === '-') {
    sign = (str[i] === '-') ? -1 : 1;
    i++;
  }

  // Convert digits
  while (i < str.length && str[i] >= '0' && str[i] <= '9') {
    result = result * 10 + (str.charCodeAt(i) - '0'.charCodeAt(0));
    i++;
  }

  return sign * result;
}

// Example usage:
console.log(atoi("   -12345")); // Output: -12345
console.log(atoi("42"));        // Output: 42
