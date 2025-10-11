def print_numbered_butterfly(rows):
    # Upper half of the butterfly
    for i in range(1, rows + 1):
        # Left wing (increasing numbers)
        for j in range(1, i + 1):
            print(j, end=" ")

        # Spaces in the middle
        for _ in range(2 * (rows - i)):
            print(" ", end=" ")

        # Right wing (increasing numbers)
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    # Lower half of the butterfly
    for i in range(rows - 1, 0, -1):
        # Left wing (increasing numbers)
        for j in range(1, i + 1):
            print(j, end=" ")

        # Spaces in the middle
        for _ in range(2 * (rows - i)):
            print(" ", end=" ")

        # Right wing (increasing numbers)
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Get input for the number of rows
num_rows = int(input("Enter the number of rows for the numbered butterfly: "))
print_numbered_butterfly(num_rows)