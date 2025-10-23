def solveNQueens(board_size):
    chessboard = [["."] * board_size for _ in range(board_size)]
    all_solutions = []
    occupied_columns = set()
    occupied_major_diagonals = set()
    occupied_minor_diagonals = set()

    def place_queens(current_row):
        if current_row == board_size:
            formatted_solution = ["".join(row) for row in chessboard]
            all_solutions.append(formatted_solution)
            return

        for current_column in range(board_size):
            if (current_column in occupied_columns or
                (current_row - current_column) in occupied_major_diagonals or
                (current_row + current_column) in occupied_minor_diagonals):
                continue

            chessboard[current_row][current_column] = "Q"
            occupied_columns.add(current_column)
            occupied_major_diagonals.add(current_row - current_column)
            occupied_minor_diagonals.add(current_row + current_column)

            place_queens(current_row + 1)

            chessboard[current_row][current_column] = "."
            occupied_columns.remove(current_column)
            occupied_major_diagonals.remove(current_row - current_column)
            occupied_minor_diagonals.remove(current_row + current_column)

    place_queens(0)
    return all_solutions
