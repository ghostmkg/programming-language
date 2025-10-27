def longest_subarray_sum_k(arr, k):
    prefix_map = {}   # prefix_sum → first_index
    current_sum = 0
    max_len = 0

    for i, num in enumerate(arr):
        current_sum += num

        # Case 1: entire prefix equals k
        if current_sum == k:
            max_len = i + 1

        # Case 2: check if a prefix with sum = current_sum - k existed
        if (current_sum - k) in prefix_map:
            length = i - prefix_map[current_sum - k]
            max_len = max(max_len, length)

        # Store first occurrence of current_sum
        if current_sum not in prefix_map:
            prefix_map[current_sum] = i

    return max_len

# Example
arr = [10, 5, 2, 7, 1, 9]
k = 15
print(longest_subarray_sum_k(arr, k))  # Output: 4
