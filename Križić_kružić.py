import random

def print_board(board):
    print("\n")
    print("     1   2   3")
    for i in range(3):
        print(f"{i+1}    {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("    -----------")
    print("\n")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves

def ai_move(board, ai_symbol):
    available = get_available_moves(board)
    player_symbol = "O" if ai_symbol == "X" else "X"

    for row, col in available:
        board[row][col] = ai_symbol
        if check_winner(board, ai_symbol):
            return (row, col)
        board[row][col] = " "

    for row, col in available:
        board[row][col] = player_symbol
        if check_winner(board, player_symbol):
            board[row][col] = " "
            return (row, col)
        board[row][col] = " "

    if (1, 1) in available:
        return (1, 1)
    
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    available_corners = [c for c in corners if c in available]
    if available_corners:
        return random.choice(available_corners)

    return random.choice(available)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    print("=== KRIŽ-KRUŽIĆ ===")

    player_symbol = random.choice(["X", "O"])
    ai_symbol = "O" if player_symbol == "X" else "X"
    
    print(f"Ti igraš sa: {player_symbol}")
    print(f"Kompjuter igra sa: {ai_symbol}")
    
    if player_symbol == "X":
        print("Počinješ ti! 🎮")
    else:
        print("Kompjuter počinje! 🤖")
    
    print("\nUnesi poziciju kao: red,stupac")
    print("Redovi: 1 (gornji), 2 (srednji), 3 (donji)")
    print("Stupci: 1 (lijevi), 2 (srednji), 3 (desni)")
    print("Primjer: 1,3 = gornji desni kut\n")
    
    while True:
        if player_symbol == "O" and all(cell == " " for row in board for cell in row):
            print("Kompjuter razmišlja...")
            row, col = ai_move(board, ai_symbol)
            board[row][col] = ai_symbol
            print(f"Kompjuter je odigrao: ({row+1},{col+1})")
            print_board(board)
            
            if check_winner(board, ai_symbol):
                print("😔 Kompjuter je pobijedio!")
                break
            
            if is_board_full(board):
                print("🤝 Neriješeno!")
                break
        else:
            print_board(board)
        
        while True:
            try:
                move = input(f"Tvoj potez (red,stupac): ").split(",")
                row = int(move[0].strip()) - 1
                col = int(move[1].strip()) - 1
                
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Unesite brojeve između 1 i 3!")
                    continue
                
                if board[row][col] != " ":
                    print("Polje je već zauzeto!")
                    continue
                
                board[row][col] = player_symbol
                break
            except (ValueError, IndexError):
                print("Neispravan unos! Pokušaj ponovno (npr. 2,2)")
        
        if check_winner(board, player_symbol):
            print_board(board)
            print("🎉 Pobijedio si!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("🤝 Neriješeno!")
            break
        
        print("Kompjuter razmišlja...")
        row, col = ai_move(board, ai_symbol)
        board[row][col] = ai_symbol
        print(f"Kompjuter je odigrao: ({row+1},{col+1})")
        print_board(board)
        
        if check_winner(board, ai_symbol):
            print("😔 Kompjuter je pobijedio!")
            break
        
        if is_board_full(board):
            print("🤝 Neriješeno!")
            break

if __name__ == "__main__":
    play_game()
