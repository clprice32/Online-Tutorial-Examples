# Simple Battleship game created in CodeAcademy: Python tutorial

# Import the necessary libraries for the game
from random import randint

# Setting up the playing board
board = []

for x in range(0, 5):
    board.append(["O"] * 5)

# Aligning the board into an evenly spaced 5x5 grid
def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

# Create the CPU's ship placement parameters
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Debugging: Displays the CPU's ship position on the board
# print ship_row
# print ship_col

# Player turns: Enter the row & column, will display if hit or miss ship & how many turns are left to play the game
# Will display the previous incorrect guesses on the board
# The player will have 4 chances to guess the placement of the CPU's ship
for turn in range(4):
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
        if turn == 3:
            print "Game Over"
    
    board[guess_row][guess_col] = "X"
    print_board(board)
