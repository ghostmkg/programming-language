function twoSum(nums, target) {
    const map = {}; // Object to store values and their indices
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (map.hasOwnProperty(complement)) {
            return [map[complement], i]; // Return indices if complement is found
        }
        map[nums[i]] = i; // Store the current number and its index
    }
    return null; // Return null if no solution is found
}

// Example usage
const nums = [2, 7, 11, 15];
const target = 9;
console.log(twoSum(nums, target)); // Output: [0, 1]
