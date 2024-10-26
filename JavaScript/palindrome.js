function isPalindrome(str) {

    str = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();


    return str === str.split('').reverse().join('');
}

// Example usage:
const word = "racecar";
if (isPalindrome(word)) {
    console.log(word + " is a palindrome.");
} else {
    console.log(word + " is not a palindrome.");
}