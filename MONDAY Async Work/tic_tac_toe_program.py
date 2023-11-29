# My tic-tac-toe game code

def intro():
#this makes the starting rules
    print("Welcome to tic tac toe!")
    print("Player 1 and 2, X and O, takes turns after another in the 3x3 grid")
    print("The first who places three in horizontal, diagnol, or vertical wins!")

def create_grid():
#Creating the grid
    print("Here is the game board")
board = [["_","_","_"]
         ["_","_","_"]
         ["_","_","_"]]
board

#display the board
def display_board():
    board = True
print(board[0] + " | " + board[1] + " | " + board[2] + "  " + "1|2|3")
print(board[3] + " | " + board[4] + " | " + board[5] + "  " + "4|5|6")
print(board[6] + " | " + board[5] + " | " + board[6] + "  " + "4|5|6")

#define players
def players():
    print("Choose your player - X or O")
    p1 = input("Player1: ")
    p2 = input("")
    if p1=="X":
        p2 = "O"
        print("Player2: " + p2)
    elif p1=="O":
        p2 = "X"
        print("Player2: " + p2)
    elif p1 != "O" or p1:
        print("Invalid character. Please choose X or O")
    players()
    
#player position
def player_position():
    global current_player
    print("current player: " + current_player)
    position = input("Choose position from 1 - 9:")

#loop

