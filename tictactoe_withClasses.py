## python3 tictactoe_withClasses.py

# GLOBAL VARS-SETTINGS
PLAYERS_SYMBOLS  = {1:'X', 2:'O'}
BOARD_SYMBOL     = '-'
PLAYER_SORT_DEF  = 2

# The main class
# Creates a 3x3 board with the BOARD_SYMBOL
# Inside there are all methods needed fot the tic tac toe game
class tictatoeGame:

    def __init__(self):
        self.board = list(9 * BOARD_SYMBOL)
        self.player_sort = PLAYER_SORT_DEF

    ## Check methods
    # This method checks if the current player won the game
    # or if the game has no winner
    def checkWinner(self):
        # the winning triple for current player
        winning_triple = 3 * PLAYERS_SYMBOLS[self.player_sort]

        # collect all possible winning 3-ples (rows, columns, diagonals)
        winning_triples = []
        for i in range(0,3):
            row    = ''.join(self.board[i*3:(i+1)*3])
            column = ''.join(self.board[i:i+7:3])
            winning_triples.append(row)
            winning_triples.append(column)
        diag1  = ''.join(self.board[0:9:4])
        diag2  = ''.join(self.board[2:7:2])
        winning_triples.append(diag1)
        winning_triples.append(diag2)

        # check if the winning triple is part of the possible triples
        if winning_triple in winning_triples:
            print(f"\n\tWinner is Player {self.player_sort}. Congratulations!\n\tThank you for playing!")
            return True
        
        # check if game has no winner
        if '-' not in self.board:
            print(f"\nIt's a toe! Thank you for playing!")
            return True
        return False
    
    # method that returns if a position on the board is empty
    def checkBoardPosIsEmpty(self, pos):
        return self.board[pos] == '-'
    
    ## Set/Update methods
    # This method switches turn between the 2 players
    def switchPlayers(self):
        self.player_sort = abs(2-self.player_sort) + 1
    
    # This method writes the players symbol on the board
    def setSymbol(self, pos):
        self.board[pos] = PLAYERS_SYMBOLS[self.player_sort]

    # This method asks from the current player to choose a valid position for their turn
    # If this position is empty, player's symbol will be placed in this position
    def playersMove(self):
        print(f"\nPlayer {self.player_sort}'s turn:")
        while True:
            try:
                row = int(input(f"\tChoose a row (1, 2, 3): "))
                col = input(f"\tChoose a column (a, b, c): ")
                col = ord(col.lower())-96
                pos = ((row-1)*3) + (col-1)
                
                if pos in range(0,9) and self.checkBoardPosIsEmpty(pos):
                    break
                else:
                    print("\tInvalid input! Please enter valid numbers and choose an empty space.")
            except ValueError:
                print("\tInvalid input! Please enter valid numbers.")
        self.setSymbol(pos)
    
    ## Print methods
    # This method prints the board
    def displayBoard(self):
        print(f'\nBoard:')
        line1 = " ".join(self.board[0:3])
        line2 = " ".join(self.board[3:6])
        line3 = " ".join(self.board[6:9])
        print(f' \ta b c\n')
        print(f'1\t{line1}')
        print(f'2\t{line2}')
        print(f'3\t{line3}')


# Creates a tictatoeGame class object and uses its methods
# to play the game.
# While there is no winner for this game, board is displayed
#  and the next player is asked to play for their turn
# When there is a winner or game is tie, a message will appear
#  and the app will close
if __name__ == '__main__':
    game = tictatoeGame()
    while(game.checkWinner() == False):
        game.displayBoard()
        game.switchPlayers()
        game.playersMove()
    game.displayBoard()
    del game