/**
 * Finds the minimum value in an array of numbers.
 * @param {number[]} arr - The array to search.
 * @returns {number} The minimum value.
 */
function findMin(arr) {
    if (!Array.isArray(arr) || arr.length === 0) {
        throw new Error('Input must be a non-empty array');
    }
    let min = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    return min;
}

// Example usage:
// console.log(findMin([3, 1, 4, 1, 5, 9])); // Output: 1

module.exports = findMin;