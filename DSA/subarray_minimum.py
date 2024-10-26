def subarray_minimum(arr):
    n = len(arr)
    if n == 0:
        return []
      
    prev_less = [-1] * n
    next_less = [n] * n
    
    stack = []
    
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        prev_less[i] = stack[-1] if stack else -1
        stack.append(i)
    
    stack = []
  
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        next_less[i] = stack[-1] if stack else n
        stack.append(i)
      
    total_min_sum = 0
    for i in range(n):
        left_count = i - prev_less[i]  
        right_count = next_less[i] - i  
        total_min_sum += arr[i] * left_count * right_count

    return total_min_sum

arr = [2, 1, 3]
print("Subarray Minimum Sum:", subarray_minimum(arr))
