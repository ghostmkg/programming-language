function twoSum(nums, target) {
    const map = {}; // Create an empty object to store the complement

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i]; // Calculate the complement
        if (map.hasOwnProperty(complement)) {
            // If the complement is found in the map, return the indices
            return [map[complement], i];
        }
        // Store the current number's index
        map[nums[i]] = i;
    }
    return null; // If no solution is found, return null
}

// Example usage
const nums = [2, 7, 11, 15];
const target = 9;
const result = twoSum(nums, target);
console.log(result); // Output: [0, 1]
