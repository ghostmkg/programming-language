def linear_search(arr, target):
    """
    Perform linear search on a list.
    Returns index if found, else -1.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    x = int(input("Enter number to search: "))
    print("Index:", linear_search(arr, x))
