def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example
nums = [2, 5, 7, 10, 13, 18, 21]
print(binary_search(nums, 13))  # Output: 4
print(s.is_empty())  # False