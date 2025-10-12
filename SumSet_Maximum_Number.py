 : Find the subset with maximum sum less than or equal to a given target.
"""

def max_subset_sum(nums, target):
    best_sum = 0
    best_set = []

    def backtrack(i, current, current_sum):
        nonlocal best_sum, best_set

        # If the sum exceeds target, stop here
        if current_sum > target:
            return
        
        # Update best subset if current sum is better
        if current_sum > best_sum:
            best_sum = current_sum
            best_set = current[:]

        # Explore remaining numbers
        for j in range(i, len(nums)):
            current.append(nums[j])
            backtrack(j + 1, current, current_sum + nums[j])
            current.pop()

    backtrack(0, [], 0)
    return best_sum, best_set


# Example usage
nums = [7, 2, 4, 9, 5]
target = 12

best_sum, best_subset = max_subset_sum(nums, target)
print(f"Target: {target}")
print(f"Best Sum: {best_sum}")
print(f"Best Subset: {best_subset}")


---
