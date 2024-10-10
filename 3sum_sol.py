def three_sum(nums):
    # Sort the input array to simplify finding unique triplets
    nums.sort()
    result = []

    # Iterate through the array with index i
    for i in range(len(nums) - 2):
        # Avoid duplicate values for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Set pointers for the current element (i), and two others (left and right)
        left, right = i + 1, len(nums) - 1

        # While loop to find pairs that sum to zero with nums[i]
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                # If the sum is zero, append the triplet to the result list
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left and right pointers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move pointers inward
                left += 1
                right -= 1

            elif total < 0:
                # If sum is less than zero, move the left pointer to the right
                left += 1
            else:
                # If sum is more than zero, move the right pointer to the left
                right -= 1

    return result

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))
