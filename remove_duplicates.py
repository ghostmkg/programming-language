def remove_duplicates(lst):
    """
    Remove duplicate elements from a list.
    """
    return list(set(lst))


if __name__ == "__main__":
    data = [1, 2, 2, 3, 4, 4, 5]
    print("Unique list:", remove_duplicates(data))
