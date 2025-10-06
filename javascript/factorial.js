// factorial.js
function factorial(n) {
  if (n < 0) return -1; // invalid input
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
}