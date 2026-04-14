import tkinter as tk
import random

# --- LOGIKA

def check_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True

    if [board[i][i] for i in range(3)].count(player) == 3:
        return True

    if [board[i][2-i] for i in range(3)].count(player) == 3:
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def ai_move(board, ai_symbol):
    available = get_available_moves(board)

    # pobjednički potez
    for row, col in available:
        board[row][col] = ai_symbol
        if check_winner(board, ai_symbol):
            board[row][col] = " "
            return (row, col)
        board[row][col] = " "

    return random.choice(available)


# --- GUI ---

root = tk.Tk()
root.title("Križić-Kružić")

board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None]*3 for _ in range(3)]

player_symbol = random.choice(["X", "O"])
ai_symbol = "O" if player_symbol == "X" else "X"
current_turn = "X"

status = tk.Label(root, text=f"Igraš kao: {player_symbol}")
status.grid(row=3, column=0, columnspan=3)

def on_click(row, col):
    global current_turn

    if board[row][col] != " ":
        return

    if current_turn != player_symbol:
        return

    # igrač
    board[row][col] = player_symbol
    buttons[row][col]["text"] = player_symbol

    if check_winner(board, player_symbol):
        status.config(text="Pobijedio si!")
        disable_all()
        return

    if is_board_full(board):
        status.config(text="Neriješeno!")
        return

    current_turn = ai_symbol
    root.after(500, ai_turn)

def ai_turn():
    global current_turn

    row, col = ai_move(board, ai_symbol)
    board[row][col] = ai_symbol
    buttons[row][col]["text"] = ai_symbol

    if check_winner(board, ai_symbol):
        status.config(text="Kompjuter je pobijedio!")
        disable_all()
        return

    if is_board_full(board):
        status.config(text="Neriješeno!")
        return

    current_turn = player_symbol

def disable_all():
    for i in range(3):
        for j in range(3):
            buttons[i][j]["state"] = "disabled"

# kreiranje gumba (grid)
for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text=" ", width=10, height=4,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

# ako AI počinje
if current_turn == ai_symbol:
    root.after(500, ai_turn)

root.mainloop()
