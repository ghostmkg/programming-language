def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

# list to be sorted, you can change it according to you
arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:", arr)
bubble_sort(arr)
print("Sorted list is:", arr)
