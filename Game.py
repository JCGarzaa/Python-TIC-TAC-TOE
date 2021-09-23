'''
This is a Tic-tac-toe game that 2 users can play within the console.
Program takes user input from numpad to assign to spots until a winner is declared
Position at the top left is 1 and bottom right is 9. Spot numbers go left to right.
'''


# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if game is still going
game_still_going = True

# Who won? or Tie?
winner = None

# Whose turn is it?
current_player = "X"


# Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play a game of tic-tac-toe
def play_game():
    display_board()

    while game_still_going:
        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print('Tie.')


# Handle a single turn of a player
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        # When number not in list of 1-9
        while position not in ["1", "2", "3", "4", "5", "6", '7', '8', '9']:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        # If chosen spot is empty
        if board[position] == "-":
            valid = True
        else:
            print("That spot is already taken.")

    board[position] = player

    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    # Set up global variables
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:

        winner = None

    return


def check_rows():
    # Set up global variables
    global game_still_going
    # Check if rows are equivalent and not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If a row has match, flag winner and game over
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner (X or O)
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


def check_columns():
    # Set up global variables
    global game_still_going
    # Check if columns are equivalent and not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If a column has match, flag winner and game over
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner (X or O)
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return


def check_diagonals():
    # Set up global variables
    global game_still_going
    # Check if diagonals are equivalent and not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # If a diagonal has match, flag winner and game over
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return the winner (X or O)
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]

    return


def check_if_tie():
    global game_still_going
    # If board is filled, end game
    if "-" not in board:
        game_still_going = False

    return


def flip_player():
    # Global variables needed
    global current_player
    # If current player is X, next is O
    if current_player == "X":
        current_player = "O"
    # If current player is O, next is X
    elif current_player == 'O':
        current_player = "X"
    return


play_game()