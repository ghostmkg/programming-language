Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. It divides the input into a sorted and an unsorted region and iteratively shrinks the unsorted region by extracting the largest (or smallest, depending on the heap type) element and moving it to the sorted region.

Here’s a simple implementation of Heap Sort in Python:

```python
# Function to heapify a subtree rooted with node i
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap with root and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

# Main function to perform heap sort
def heap_sort(arr):
    n = len(arr)

    # Build a maxheap by calling heapify from the last non-leaf node downwards
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Move the current root (largest) to the end
        arr[i], arr[0] = arr[0], arr[i]
        # Call heapify on the reduced heap
        heapify(arr, i, 0)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", arr)
```

### Explanation:
1. **heapify(arr, n, i)**: This function turns a subtree into a max heap. It assumes that the binary trees rooted at left and right are already heaps, and fixes the heap property at the root.
   
2. **heap_sort(arr)**: First, we build a max heap from the input array. After building the heap, we repeatedly swap the first (largest) element with the last unsorted element and reduce the heap size, then heapify the root element again.

### Output:
```
Sorted array: [5, 6, 7, 11, 12, 13]
```

This sorts the array in ascending order using a max heap.
