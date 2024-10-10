import tkinter

def set_title(row,column):
    if game_over:
        return
    global currentPlayer
    
    # Taken spot
    if board[row][column]["text"] != "": 
        return
    
    board[row][column]["text"] = currentPlayer
    
    #switch player
    if currentPlayer == playerO:
        currentPlayer = playerX
    else:
        currentPlayer = playerO

    label["text"] = currentPlayer+"'s turn"

    # check winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    # horizontally check 3 rows
    for row in range(3):
        if board[row][0]["text"]== board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"]!="":
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow,background=color_ligh_gray)
            game_over = True
            return
        
    # vertically check 3 columns
    for column in range(3):
        if board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != "":
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow,background=color_ligh_gray)
            game_over = True
            return
        
    # Diagonally check
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] !="":
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow,background=color_ligh_gray)
        game_over = True
        return
    
     #anti-diagionally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_ligh_gray)
        board[1][1].config(foreground=color_yellow, background=color_ligh_gray)
        board[2][0].config(foreground=color_yellow, background=color_ligh_gray)
        game_over = True
        return
    
    
    #tie
    if (turns == 9):
        game_over = True
        label.config(text="Tie!", foreground=color_yellow)
    
def new_game():
    global game_over,turns
    turns = 0
    game_over = False

    label.config(text=currentPlayer+"'s turn", foreground="white")
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)

playerX = "X"
playerO = "O"
currentPlayer = playerX

board = [["0","0","0"],
          ["0","0","0"],
          ["0","0","0"]]

turns = 0
game_over = False

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_ligh_gray = "#646464"

window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False,False)


frame = tkinter.Frame(window)
label = tkinter.Label(frame,text=currentPlayer+"'s turn",font=("Consolas",20), background= color_gray,foreground="white")
label.grid(row=0,column=0,columnspan=3,sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame,text="",font=("Consolas",50,"bold"),background= color_gray,foreground=color_blue,width=4,height=1,
                                            command=lambda row=row, column=column:set_title(row,column))
        board[row][column].grid(row = row+1,column = column)

button = tkinter.Button(frame,text="Restart",font=("Consolas",20), background= color_gray,foreground="white",command=new_game)
button.grid(row=4,column=0,columnspan=3,sticky="we")

frame.pack()

# center the window

window.update()
window_width = window.winfo_width() 
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#formate
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()