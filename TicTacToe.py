# -----Global Variables -----------



#board

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# If game still going
game_still_going = True

# Who one? or Tie?
winner = None

# Whos turn is it?
current_player = 'X'

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():

    #display inital board
    display_board()

    while game_still_going:

        # handle singe turn of arbitrary player
        handle_turn(current_player)

        #check if game has ended
        check_if_game_over()

        # Flip to other player
        flip_player()

    # The game has ended
    if winner == 'X' or winner == 'O':
        print(winner + " Won!")
    elif winner == None:
        print("Tie")


def handle_turn(player):

    print(player + "'s Turn")
    position = input('Choose a position from 1-9: ')

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Taken - Please Try Again: ")

    board[position] = player

    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():

    #set global variable
    global winner
    #check rows
    row_winner = check_rows()

    #check columns
    column_winner = check_columns()

    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        #there was a winner
        winner = row_winner

    elif column_winner:
        # there was a winner
        winner = column_winner

    elif diagonal_winner:
        # there was a winner
        winner = diagonal_winner
    return

def check_rows():
    # set global variable
    global game_still_going
    # check if rows have same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    # return winner of x or o
    if row_1:
        return board[0]

    if row_2:
        return board[3]

    if row_3:
        return board[6]


    return

def check_columns():
    # set global variable
    global game_still_going
    # check if rows have same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    # return winner of x or o
    if column_1:
        return board[0]

    if column_2:
        return board[3]

    if column_3:
        return board[6]
    return

def check_diagonals():
    # set global variable
    global game_still_going
    # check if rows have same value
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False

    # return winner of x or o
    if diagonal_1:
        return board[0]

    if diagonal_2:
        return board[6]

    return

def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False

    return


def flip_player():

    global  current_player

    if current_player == 'X':
        current_player = 'O'

    elif current_player == 'O':
        current_player = 'X'

    return

play_game()

#display board


#play game


#handle turn


#check win
    #check rows
    #check columns
    #check diagonals


#check tie


#flip player

