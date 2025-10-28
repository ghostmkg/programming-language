def permute(nums):
    res = []
    n = len(nums)
    def backtrack(start):
        if start == n:
            res.append(nums[:])  
            return
        for i in range(start, n):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    backtrack(0)
    return res

# Example usage:
nums = [1, 2, 3]
print(permute(nums))  # Output: All permutations of [1, 2, 3]
# Output: All permutations of [1, 2, 3]
# time complexity: O(n * n!)
# space complexity: O(n!)

