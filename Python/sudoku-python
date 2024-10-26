def is_valid_row(board, row):
    #Checks if a row contains unique digits
    digits = set()
    for col in range(9):
        if board[row][col] in digits:
            return False
        digits.add(board[row][col])
    return True

def is_valid_col(board, col):
   #Checks if a column contains unique digits
    digits = set()
    for row in range(9):
        if board[row][col] in digits:
            return False
        digits.add(board[row][col])
    return True

def is_valid_block(board, row, col):
    #Checks if a 3x3 block contains unique digits
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    digits = set()
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] in digits:
                return False
            digits.add(board[i][j])
    return True

def is_valid_board(board):
    #Checks if the entire Sudoku board is valid
    for row in range(9):
        if not is_valid_row(board, row):
            return False
    for col in range(9):
        if not is_valid_col(board, col):
            return False
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not is_valid_block(board, row, col):
                return False
    return True

def find_empty_cell(board):
    #Finds the next empty cell (represented by 0) on the board
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def solve_sudoku(board):
    #Solves a Sudoku puzzle using backtracking
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
  # Puzzle is solved
    row, col = empty_cell

    for num in range(1, 10):
        if is_valid_row(board,row) and is_valid_col(board, col) and is_valid_block(board, row, col):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack
    return False

# Example usage:
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(board):
    print("Solution found:")
    for row in board:
        print(row)
else:
    print("No solution exists.")
