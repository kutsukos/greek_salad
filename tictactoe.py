## python3 tictactoe.py

# GLOBAL VARS-SETTINGS
PLAYERS_SYMBOLS  = {1:'X', 2:'O'}
BOARD_SYMBOL     = '-'
PLAYER_SORT      = 2

# This methods prints the board
def display_board(board):
    print(f'\nBoard:')
    line1 = " ".join(board[0:3])
    line2 = " ".join(board[3:6])
    line3 = " ".join(board[6:9])
    print(f' \ta b c\n')
    print(f'1\t{line1}')
    print(f'2\t{line2}')
    print(f'3\t{line3}')

# This method checks if the current player won the game
# or if the game has no winner
def check_winner(board):
    # the winning triple for current player
    winning_triple = 3 * PLAYERS_SYMBOLS[PLAYER_SORT]

    # collect all possible winning 3-ples (rows, columns, diagonals)
    winning_triples = []
    for i in range(0,3):
        row    = ''.join(board[i*3:(i+1)*3])
        column = ''.join(board[i:i+7:3])
        winning_triples.append(row)
        winning_triples.append(column)
    diag1  = ''.join(board[0:9:4])
    diag2  = ''.join(board[2:7:2])
    winning_triples.append(diag1)
    winning_triples.append(diag2)
   
    if winning_triple in winning_triples:
        print(f"\n\tWinner is Player {PLAYER_SORT}. Congratulation!\n\tThank you for playing!")
        return True
    
    # check if game has no winner
    if '-' not in board:
        print(f"\nIt's a toe! Thank you for playing!")
        return True
    return False

# This function switches turn between the 2 players
def change_player():
    global PLAYER_SORT
    PLAYER_SORT = abs(2-PLAYER_SORT) +1

# This method asks from the current player to choose a valid position for their turn
# If this position is empty, player's symbol will be placed in this position
def players_move(board):
    print(f"\nPlayer {PLAYER_SORT}'s turn:")
    while True:
        try:
            row = int(input(f"\tChoose a row (1, 2, 3): "))
            col = input(f"\tChoose a column (a, b, c): ")
            col = ord(col.lower())-96
            pos = ((row-1)*3) + (col-1)
            
            if pos in range(0,9) and board[pos]=='-':
                break
            else:
                print("\tInvalid input! Please enter valid numbers and choose an empty space.")
        except ValueError:
            print("\tInvalid input! Please enter valid numbers.")
    board[pos] = PLAYERS_SYMBOLS[PLAYER_SORT]

# The main method
# Creates a 3x3 board with the BOARD_SYMBOL
# While there is no winner for this game, board is displayed
#  and the next player is asked to play for their turn
# When there is a winner or game is tie, a message will appear
#  and the app will close
def main():
    board = list(9*BOARD_SYMBOL)
    while(check_winner(board)==False):
        display_board(board)
        change_player()
        players_move(board)
    return 1

main()