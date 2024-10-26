def next_smaller_elements(arr):
    n = len(arr)
    result = [-1] * n  # Initialize result with -1
    stack = []

    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        # Pop elements from the stack that are greater than or equal to the current element
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        # If the stack is not empty, the top element is the next smaller element
        if stack:
            result[i] = stack[-1]

        # Push the current element onto the stack
        stack.append(arr[i])

    return result

# Example usage
arr = [4, 8, 5, 2, 25]
print("Array:", arr)
print("Next Smaller Elements:", next_smaller_elements(arr))
