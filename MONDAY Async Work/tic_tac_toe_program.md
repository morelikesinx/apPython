# My tic-tac-toe game code

def intro():
#this makes the starting rules
    print("Welcome to tic tac toe!)
    print("Player 1 and 2, X and O, takes turns after another in the 3x3 grid")
    print("The first who places three in horizontal, diagnol, or vertical wins!")

def create-grid():
#Creating the grid
    print("Here is the game board")
    board = [["_","_","_"]
             ["_","_","_"]
             ["_","_","_"]]
    return board

#display the board
    def display_board():
        print(board[0] + " | " + board[1] + " | " board[2] + "  " + "1|2|3")
        print(board[3] + " | " + board[4] + " | " board[5] + "  " + "4|5|6")
        print(board[6] + " | " + board[5] + " | " board[6] + "  " + "4|5|6")