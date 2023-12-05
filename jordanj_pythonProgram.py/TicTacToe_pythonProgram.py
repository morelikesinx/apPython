print("Jordan's Tic Tac Toe")

#game board
board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

#game indicator
game_on = True

# Initialize player
current_player = "X"

#Display game board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + "    " + "1|2|3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "    " + "4|5|6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "    " + "7|8|9")
#define players
def players():
    print("Select Player - X or O")
    p1 = input("Player1: ")
    p2 = ""
    if p1 == "X":
        p2 = "O"
        print("Player2: " + p2)
    elif p1 == "O":
        p2 = "X"
        print("Player2: " + p2)
    elif p1 != "O" or p1 != "X":
        print("Invalid. Type X or O")
        play_game()

#Player position
def player_position():
    global current_player
    print("Current Player: " + current_player)
    position = input("Choose position from 1 - 9: ")

    # Loop until win or tie
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
          position = input("Choose position from 1 - 9: ")
        position = int(position) - 1

        if board[position] == "_":
            valid = True
        else:
            print("Position already selected, choose another position!")
    board[position] = current_player
    display_board()

#play game function 
def play_game():
    print("Jordan's Tic Tac Toe Game")
    display_board()
    players()
    
  #flip players until there is a win
    while game_on:
        player_position()
        
        #Check winner
        def check_winner():
            global game_on
            #Check rows for win
            if board[0] == board[1] == board[2] != "_":
                game_on = False
                print("Congrats! " + board[0]+" you won!")
            elif board[3] == board[4] == board[5] != "_":
                game_on = False
                print("Congrats! " + board[3]+" you won!")
            elif board[6] == board[7] == board[8] != "_":
                game_on = False
                print("Congrats! " + board[6]+" you won!")
             #Check columns for win
            elif board[0] == board[3] == board[6] != "_":
                game_on = False
                print("Congrats! " + board[0]+" you won!")
            elif board[1] == board[4] == board[7] != "_":
                game_on = False
                print("Congrats! " + board[1]+" you won!")
            elif board[2] == board[5] == board[8] != "_":
                game_on = False
                print("Congrats! " + board[2]+" you won!")
             #Check diagonals for win
            elif board[0] == board[4] == board[8] != "_":
                game_on = False
                print("Congrats! " + board[0]+" you won!")
            elif board[2] == board[4] == board[6] != "_":
                game_on = False
                print("Congrats! "+ board[6]+" you won!")
             #If none of the above, its a tie
            elif "_" not in board:
                game_on = False
                print("It's a Tie")
                exit()

        #flip player
        def flip_player():
            global current_player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        flip_player()
        check_winner()
#Play the game
play_game()