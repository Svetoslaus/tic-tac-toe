board = ["",
         "1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

player = "X"
run = True
def print_board():
    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])

def turn():
    global run
    while True:
        player_turn = input("Please, give your number: ")
        if player_turn == "q":
            run = False
            return None
        player_turn = int(player_turn)
        if player_turn >= 1 and player_turn <= 9:
            if board[player_turn] == "X" or board[player_turn] == "O":
                print("This field is already chosen. Please, repeat your turn!")
            return player_turn
        else:
            print("The number must to be between 1 and 9. Please, repeat your turn.")
def change():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

def win():
    # lines
    if board[1] == board[2] == board[3]:
        return board[1]
    if board[4] == board[5] == board[6]:
        return board[4]
    if board[7] == board[8] == board[9]:
        return board[7]

    # columns
    if board[1] == board[4] == board[7]:
        return board[1]
    if board[2] == board[5] == board[8]:
        return board[2]
    if board[3] == board[6] == board[9]:
        return board[3]
    # diagonal
    if board[1] == board[5] == board[9]:
        return board[1]
    if board[3] == board[5] == board[7]:
        return board[3]

def draw():
    if board[1] != "1" and board[2] != "2" and board[3] != "3" and board[4] != "4" and board[5] != "5" and board[6] != "6" and board[7] != "7" and board[8] != "8" and board[9] != "9":
     return True

while run:
    print_board()
    player_turn = turn()
    if player_turn != None:
        board[player_turn] = player
        winner = win()
        if winner:
            print("Congrats! " + winner + " wins")
            run = False
        if draw():
            print("Draw! There is no winner!")
            run = False
        change()



print(turn())
