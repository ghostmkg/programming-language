# Sudoku solver using backtracking.
# This cell implements a solver and demonstrates it on a sample Sudoku puzzle.
# Replace the `board` variable with any 9x9 puzzle (0 = empty) to solve your own puzzle.

def print_board(b):
    for i, row in enumerate(b):
        line = ""
        for j, val in enumerate(row):
            ch = str(val) if val != 0 else "."
            line += ch + (" " if (j+1)%3 else " | ")
        print(line.rstrip(" | "))
        if (i+1) % 3 == 0 and i != 8:
            print("-"*21)

def find_empty(b):
    for i in range(9):
        for j in range(9):
            if b[i][j] == 0:
                return i, j
    return None

def valid(b, row, col, num):
    # check row
    if any(b[row][c] == num for c in range(9)):
        return False
    # check column
    if any(b[r][col] == num for r in range(9)):
        return False
    # check 3x3 box
    box_r = (row // 3) * 3
    box_c = (col // 3) * 3
    for r in range(box_r, box_r + 3):
        for c in range(box_c, box_c + 3):
            if b[r][c] == num:
                return False
    return True

def solve_sudoku(b):
    empty = find_empty(b)
    if not empty:
        return True  # solved
    r, c = empty
    for num in range(1, 10):
        if valid(b, r, c, num):
            b[r][c] = num
            if solve_sudoku(b):
                return True
            b[r][c] = 0  # backtrack
    return False

# Example Sudoku (0 denotes empty). This is a commonly used hard example.
board = [
    [0,0,0, 2,6,0, 7,0,1],
    [6,8,0, 0,7,0, 0,9,0],
    [1,9,0, 0,0,4, 5,0,0],
    [8,2,0, 1,0,0, 0,4,0],
    [0,0,4, 6,0,2, 9,0,0],
    [0,5,0, 0,0,3, 0,2,8],
    [0,0,9, 3,0,0, 0,7,4],
    [0,4,0, 0,5,0, 0,3,6],
    [7,0,3, 0,1,8, 0,0,0],
]

print("Given puzzle:\n")
print_board(board)
print("\nSolving...\n")

if solve_sudoku(board):
    print("Solved Sudoku:\n")
    print_board(board)
else:
    print("No solution exists for the given puzzle.")
