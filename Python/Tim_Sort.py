MIN_RUN = 32

def insertion_sort(arr, left, right):
    """
    Perform insertion sort on a subarray from index 'left' to 'right'.
    
    Args:
        arr (list): The list to be sorted.
        left (int): The starting index of the subarray.
        right (int): The ending index of the subarray.
    """
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def merge(arr, left, mid, right):
    """
    Merge two sorted subarrays into a single sorted array.
    
    Args:
        arr (list): The original array with two sorted subarrays.
        left (int): The starting index of the left subarray.
        mid (int): The ending index of the left subarray and middle point.
        right (int): The ending index of the right subarray.
    """
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    
    i = 0
    j = 0
    k = left
    
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

def tim_sort(arr):
    """
    Perform TimSort on the input array.
    
    TimSort is a hybrid sorting algorithm derived from merge sort and insertion sort. It sorts smaller chunks using insertion sort, then merges them using a merge sort.
    
    Args:
        arr (list): The list to be sorted.
    """
    n = len(arr)
    

    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)
    

    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(left + 2 * size - 1, n - 1)
            
            if mid < right:
                merge(arr, left, mid, right)
        
        size *= 2

# Test cases
if __name__ == "__main__":
    def test_tim_sort():
        test_cases = [
            ([12, 11, 13, 5, 6, 7], [5, 6, 7, 11, 12, 13]),    # Random order
            ([], []),                                          # Empty array
            ([1], [1]),                                        # Single element
            ([3, 1, 2], [1, 2, 3]),                           # Small array
            ([5, 5, 5, 5], [5, 5, 5, 5]),                     # All elements the same
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),               # Already sorted
            ([9, 7, 5, 3, 1], [1, 3, 5, 7, 9])                # Reverse order
        ]
        
        for i, (input_data, expected) in enumerate(test_cases):
            tim_sort(input_data)
            assert input_data == expected, f"Test case {i+1} failed: {input_data} != {expected}"
            print(f"Test case {i+1} passed.")
    
    test_tim_sort()
