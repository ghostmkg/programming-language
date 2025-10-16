#!/usr/bin/env python3
"""
Tic-Tac-Toe terminal game
- Play 2-player (human vs human) or vs computer (human vs AI).
- AI uses minimax algorithm (plays optimally).
Usage:
    python tic_tac_toe.py
"""

from typing import List, Optional, Tuple

# Board positions: indexes 0..8 representing:
#  1 | 2 | 3
#  ---------
#  4 | 5 | 6
#  ---------
#  7 | 8 | 9

def print_board(board: List[str]) -> None:
    """Prints the board in a user-friendly format."""
    def cell(i):
        return board[i] if board[i] != " " else str(i + 1)
    print()
    print(f" {cell(0)} | {cell(1)} | {cell(2)} ")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)} ")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)} ")
    print()

def check_winner(board: List[str]) -> Optional[str]:
    """Returns 'X' or 'O' if there's a winner, 'Draw' if full without winner, else None."""
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if all(cell != " " for cell in board):
        return "Draw"
    return None

def available_moves(board: List[str]) -> List[int]:
    return [i for i, v in enumerate(board) if v == " "]

def minimax(board: List[str], player: str, maximizing: bool) -> Tuple[int, Optional[int]]:
    """
    Minimax algorithm.
    Returns a tuple (score, move_index).
    Scores: +1 => 'X' win, -1 => 'O' win, 0 => draw.
    We will assume AI symbol is provided when calling best_move().
    """
    winner = check_winner(board)
    if winner == "X":
        return 1, None
    if winner == "O":
        return -1, None
    if winner == "Draw":
        return 0, None

    if maximizing:
        best_score = -float('inf')
        best_move = None
        for m in available_moves(board):
            board[m] = player
            score, _ = minimax(board, "O" if player == "X" else "X", False)
            board[m] = " "
            if score > best_score:
                best_score = score
                best_move = m
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        for m in available_moves(board):
            board[m] = player
            score, _ = minimax(board, "O" if player == "X" else "X", True)
            board[m] = " "
            if score < best_score:
                best_score = score
                best_move = m
        return best_score, best_move

def best_move_for_ai(board: List[str], ai_symbol: str) -> int:
    """Returns best move index for AI using minimax."""
    maximizing = True if ai_symbol == "X" else False
    _, move = minimax(board, ai_symbol, maximizing)
    # fallback: choose first available if minimax somehow returns None
    return move if move is not None else (available_moves(board)[0] if available_moves(board) else -1)

def human_move(board: List[str], symbol: str) -> None:
    """Prompts human for a move and places it on the board."""
    while True:
        try:
            choice = input(f"Player {symbol}, enter your move (1-9): ").strip()
            if choice.lower() in ("q", "quit", "exit"):
                print("Goodbye!")
                exit(0)
            pos = int(choice) - 1
            if pos not in range(9):
                print("Invalid input: choose a number from 1 to 9.")
                continue
            if board[pos] != " ":
                print("That cell is already taken. Pick another.")
                continue
            board[pos] = symbol
            break
        except ValueError:
            print("Please enter a valid number (1-9) or 'q' to quit.")

def play_game() -> None:
    print("Welcome to Tic-Tac-Toe!")
    print("Options:")
    print(" 1) Human vs Human")
    print(" 2) Human vs Computer (AI)")
    while True:
        mode = input("Choose mode (1 or 2): ").strip()
        if mode in ("1", "2"):
            break
        print("Please enter 1 or 2.")

    # Choose symbols
    while True:
        first = input("Do you want to play as X and go first? (y/n): ").strip().lower()
        if first in ("y", "n"):
            break
        print("Enter 'y' or 'n'.")

    if first == "y":
        human_symbol = "X"
        ai_symbol = "O"
    else:
        human_symbol = "O"
        ai_symbol = "X"

    board = [" "] * 9
    current = "X"  # X always goes first

    if mode == "1":
        # Two humans
        print_board(board)
        while True:
            human_move(board, current)
            print_board(board)
            winner = check_winner(board)
            if winner:
                if winner == "Draw":
                    print("It's a draw!")
                else:
                    print(f"Player {winner} wins! 🎉")
                break
            current = "O" if current == "X" else "X"
    else:
        # Human vs AI
        print("\nStarting Human vs Computer (AI).")
        print(f"You are '{human_symbol}'. AI is '{ai_symbol}'.")
        print_board(board)

        while True:
            if current == human_symbol:
                human_move(board, human_symbol)
                print_board(board)
            else:
                print("AI is thinking...")
                move = best_move_for_ai(board, ai_symbol)
                if move == -1:
                    print("No moves left.")
                else:
                    board[move] = ai_symbol
                    print(f"AI placed {ai_symbol} in cell {move + 1}.")
                print_board(board)

            winner = check_winner(board)
            if winner:
                if winner == "Draw":
                    print("It's a draw!")
                else:
                    if winner == human_symbol:
                        print("You win! 🎉")
                    else:
                        print("AI wins. Better luck next time!")
                break
            current = "O" if current == "X" else "X"

if __name__ == "__main__":
    play_game()
