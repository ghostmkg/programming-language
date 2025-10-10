
# ------------------------------------------------------------
# Problem: Two Sum
# Source: LeetCode #1
# Difficulty: Easy
# ------------------------------------------------------------
# Statement:
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# Example:
#   Input: nums = [2,7,11,15], target = 9
#   Output: [0,1]  # Because nums[0] + nums[1] == 9
#
# Approach:
#   - Use a hash map (dictionary in Python) to store
#     each number's index as we iterate.
#   - For each number, check if (target - current number)
#     already exists in the map.
#   - If yes, return the stored index and the current index.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ------------------------------------------------------------

def two_sum(nums, target):
    seen = {}  # Dictionary to store value:index pairs
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]  # Found the pair
        seen[num] = i  # Store current number's index
    return []  # No valid pair found


# ------------------------------------------------------------
# Driver Code for Testing
# ------------------------------------------------------------
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("Input:", nums)
    print("Target:", target)
    print("Output Indices:", two_sum(nums, target))
