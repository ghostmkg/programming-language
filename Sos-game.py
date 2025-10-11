import tkinter as tk
from tkinter import simpledialog
import random

class SOSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 SOS Game - Competitive AI")
        self.create_new_game()

    def create_new_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Limit board size for scrollable view
        self.size = simpledialog.askinteger("Board Size", "Enter board size (3-12):", minvalue=3, maxvalue=12)
        self.board = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.buttons = [[None for _ in range(self.size)] for _ in range(self.size)]

        self.player_score = 0
        self.computer_score = 0
        self.turn = "Player"
        self.player_choice = None
        self.move_history = []

        # Scoreboard frame
        score_frame = tk.Frame(self.root, bd=2, relief="groove", padx=10, pady=5)
        score_frame.pack(pady=5, fill="x")
        self.player_label = tk.Label(score_frame, text=f"Player: {self.player_score}", font=("Helvetica", 12, "bold"), fg="blue")
        self.player_label.pack(side=tk.LEFT, padx=10)
        self.computer_label = tk.Label(score_frame, text=f"Computer: {self.computer_score}", font=("Helvetica", 12, "bold"), fg="red")
        self.computer_label.pack(side=tk.LEFT, padx=10)
        self.turn_label = tk.Label(score_frame, text="Your Turn!", font=("Helvetica", 12, "italic"))
        self.turn_label.pack(side=tk.LEFT, padx=20)

        # Move history panel
        history_frame = tk.Frame(self.root, bd=2, relief="groove")
        history_frame.pack(pady=5)
        tk.Label(history_frame, text="Move History", font=("Helvetica", 10, "bold")).pack()
        self.history_text = tk.Text(history_frame, width=35, height=8, state='disabled', bd=1, relief="sunken")
        self.history_text.pack()

        # Choice frame
        choice_frame = tk.Frame(self.root)
        choice_frame.pack(pady=5)
        tk.Label(choice_frame, text="Choose your letter: ").pack(side=tk.LEFT)
        tk.Button(choice_frame, text="S", font=("Arial", 14, "bold"), width=3, command=lambda: self.choose_letter("S")).pack(side=tk.LEFT, padx=5)
        tk.Button(choice_frame, text="O", font=("Arial", 14, "bold"), width=3, command=lambda: self.choose_letter("O")).pack(side=tk.LEFT, padx=5)

        # Scrollable Board Frame
        canvas = tk.Canvas(self.root, width=400, height=400)
        canvas.pack(side=tk.LEFT, fill="both", expand=True)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.board_frame = tk.Frame(canvas)
        canvas.create_window((0,0), window=self.board_frame, anchor="nw")

        for r in range(self.size):
            for c in range(self.size):
                btn = tk.Button(self.board_frame, text=" ", font=("Arial", 14, "bold"),
                                width=4, height=2, command=lambda row=r, col=c: self.player_move(row, col))
                btn.grid(row=r, column=c, padx=1, pady=1)
                self.buttons[r][c] = btn

        tk.Button(self.root, text="Restart Game", font=("Helvetica", 12), command=self.create_new_game).pack(pady=5)

    def choose_letter(self, letter):
        self.player_choice = letter

    def update_dashboard(self):
        self.player_label.config(text=f"Player: {self.player_score}")
        self.computer_label.config(text=f"Computer: {self.computer_score}")
        self.turn_label.config(text="Your Turn!" if self.turn == "Player" else "Computer's Turn")
        self.update_history_panel()

    def update_history_panel(self):
        self.history_text.config(state='normal')
        self.history_text.delete(1.0, tk.END)
        for move in self.move_history:
            self.history_text.insert(tk.END, move + "\n")
        self.history_text.config(state='disabled')

    def player_move(self, row, col):
        if self.turn != "Player" or self.board[row][col] != " ":
            return
        if not self.player_choice:
            return

        self.board[row][col] = self.player_choice
        self.buttons[row][col]["text"] = self.player_choice
        self.move_history.append(f"Player: {self.player_choice} at ({row+1},{col+1})")

        scored, cells = self.check_sos_highlight(row, col)
        if scored > 0:
            self.player_score += scored
            self.highlight_cells(cells, "blue")
        else:
            self.turn = "Computer"

        self.update_dashboard()
        self.player_choice = None

        if self.is_full():
            self.show_winner()
            return

        if self.turn == "Computer":
            self.root.after(500, self.computer_move)

    def computer_move(self):
        move = self.competitive_ai()
        if move:
            row, col, letter = move
            self.board[row][col] = letter
            self.buttons[row][col]["text"] = letter
            self.move_history.append(f"Computer: {letter} at ({row+1},{col+1})")

        scored, cells = self.check_sos_highlight(row, col)
        if scored > 0:
            self.computer_score += scored
            self.highlight_cells(cells, "red")
            self.root.after(500, self.computer_move)
        else:
            self.turn = "Player"

        self.update_dashboard()
        if self.is_full():
            self.show_winner()

    # Competitive AI logic (same as previous)
    def competitive_ai(self):
        empty = [(r, c) for r in range(self.size) for c in range(self.size) if self.board[r][c] == " "]
        for r, c in empty:
            for letter in ["S", "O"]:
                self.board[r][c] = letter
                scored, _ = self.check_sos_highlight(r, c)
                if scored > 0:
                    self.board[r][c] = " "
                    return (r, c, letter)
                self.board[r][c] = " "
        for r, c in empty:
            for letter in ["S", "O"]:
                self.board[r][c] = letter
                if self.player_can_sos():
                    self.board[r][c] = " "
                    return (r, c, letter)
                self.board[r][c] = " "
        best_score = -1
        best_move = None
        for r, c in empty:
            for letter in ["S", "O"]:
                self.board[r][c] = letter
                score = self.simulate_future_score()
                if score > best_score:
                    best_score = score
                    best_move = (r, c, letter)
                self.board[r][c] = " "
        if best_move:
            return best_move
        r, c = random.choice(empty)
        letter = random.choice(["S", "O"])
        return (r, c, letter)

    def player_can_sos(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == " ":
                    for letter in ["S", "O"]:
                        self.board[r][c] = letter
                        scored, _ = self.check_sos_highlight(r, c)
                        if scored > 0:
                            self.board[r][c] = " "
                            return True
                        self.board[r][c] = " "
        return False

    def simulate_future_score(self):
        score = 0
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == " ":
                    for letter in ["S", "O"]:
                        self.board[r][c] = letter
                        s, _ = self.check_sos_highlight(r, c)
                        score += s
                        self.board[r][c] = " "
        return score

    def check_sos_highlight(self, row, col, board=None):
        if board is None:
            board = self.board
        n = self.size
        count = 0
        highlight_cells = []
        dirs = [(0,1),(1,0),(1,1),(1,-1),(0,-1),(-1,0),(-1,-1),(-1,1)]
        for dr, dc in dirs:
            r1, c1 = row-dr, col-dc
            r2, c2 = row+dr, col+dc
            if 0<=r1<n and 0<=r2<n and 0<=c1<n and 0<=c2<n:
                if board[r1][c1]=="S" and board[row][col]=="O" and board[r2][c2]=="S":
                    count +=1
                    highlight_cells.append([(r1,c1),(row,col),(r2,c2)])
        flat_cells = [cell for group in highlight_cells for cell in group]
        return count, flat_cells

    def highlight_cells(self, cells, color):
        for r, c in cells:
            self.buttons[r][c].config(bg=color)
        self.root.after(500, lambda: self.remove_highlight(cells))

    def remove_highlight(self, cells):
        for r, c in cells:
            self.buttons[r][c].config(bg="SystemButtonFace")

    def is_full(self):
        return all(self.board[r][c] != " " for r in range(self.size) for c in range(self.size))

    def show_winner(self):
        popup = tk.Toplevel(self.root)
        popup.title("🏆 Game Over 🏆")
        popup.geometry("350x200")
        popup.resizable(False, False)
        popup.grab_set()

        frame = tk.Frame(popup, bd=3, relief="solid", padx=20, pady=20, bg="#f0f0f0")
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        if self.player_score > self.computer_score:
            winner_text = "🎉 You win!"
        elif self.player_score < self.computer_score:
            winner_text = "🤖 Computer wins!"
        else:
            winner_text = "🤝 It's a draw!"

        tk.Label(frame, text=winner_text, font=("Helvetica", 16, "bold"), fg="green").pack(pady=5)
        tk.Label(frame, text=f"Player Score: {self.player_score}\nComputer Score: {self.computer_score}",
                 font=("Helvetica", 14), fg="blue").pack(pady=5)
        tk.Button(frame, text="Play Again", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white",
                  command=lambda: [popup.destroy(), self.create_new_game()]).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    game = SOSGame(root)
    root.mainloop()
