
# Since I have an interest in combinatorial game theory and chess, my end goal would be to create the strongest chess
# engine that I could possible make. Of course, this will take a while since I have only just begun my studies in
# mathematics and have a baby's worth of knowledge in Python and zero knowledge in machine learning. This is a first
# step in my learning process. This program is a tic-tac-toe playing program where I can practice coding in Python and
# create combinatorial games such as tic-tac-toe. At this present stage in the process, the game has no definitive
# GUI and lacks efficiency in the code. Eventually I will clean all of it up and perhaps create my own bot/algorithm or
# whatever you may call it using machine learning to solve tic-tac-toe myself.

# This is currently the first version and I only spent like 30 minutes making it so disregard any horrid coding.

# Imports numpy for 3x3 array.
import numpy as np

# Creates the board which is a 3x3 array where all empty positions are denoted as 0.
# Player 1 positions are denoted as 1.
# Player 2 positions are denoted as 2.
board = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
])


# This is the main function where the program will receive all user inputs and edit board.
def main():
    player_move = int(input("Which player's turn is it?: "))  # Receives input to determine which player to move.

    if player_move == 1:  # If it is player 1's turn to play...
        player_1_row_move = input("Please enter the row for player 1: ")  # Receives input for row to be played.
        player_1_column_move = input("Please enter the column for player 1: ")  # Receives input for column.

        # If chosen position is empty then it will change the value of the element to player's value, in this case = 1.
        # If chosen position is not empty, then it will print an error message and will call the win_check function...
        # which itself calls the main function again to play.
        if board[((int(player_1_row_move)) - 1), ((int(player_1_column_move)) - 1)] == 0:
            board[((int(player_1_row_move)) - 1), ((int(player_1_column_move)) - 1)] = 1
        elif board[((int(player_1_row_move)) - 1), ((int(player_1_column_move)) - 1)] != 0:
            print("ERROR: Spot already played!")

        win_check()  # Calls win condition function.

    elif player_move == 2:  # Same code but for player 2.
        player_2_row_move = input("Please enter the row for player 2: ")
        player_2_column_move = input("Please enter the column for player 2: ")

        # I feel like this portion is really messy with:
        # --> board[((int(player_2_row_move)) - 1), ((int(player_2_column_move)) - 1)]...
        # So I want to clean it up later on.
        if board[((int(player_2_row_move)) - 1), ((int(player_2_column_move)) - 1)] == 0:
            board[((int(player_2_row_move)) - 1), ((int(player_2_column_move)) - 1)] = 2
        elif board[((int(player_2_row_move)) - 1), ((int(player_2_column_move)) - 1)] != 0:
            print("ERROR: Spot already played!")

        win_check()

    else:  # If player number is not 1 or 2 then it will print an error message and call main function again.
        print("ERROR: Invalid player number detected!")
        main()


# This is a function that will check the winning conditions for the player.
# I know this is really messy and garbage code but I will go back...
# ...and clean it up with a more efficient for-loop or something.
def win_check():
    if (board[0, 0] & board[0, 1] & board[0, 2]) == 1:  # IF TOP ROW CLEAR FOR PLAYER 1
        print("PLAYER 1 WINS!")  # Winner announcement.
        print(board)  # Prints winning board.

    elif (board[0, 0] & board[0, 1] & board[0, 2]) == 2:  # IF TOP ROW CLEAR FOR PLAYER 2
        print("PLAYER 2 WINS!")
        print(board)

    elif (board[1, 0] & board[1, 1] & board[1, 2]) == 1:  # IF MIDDLE ROW CLEAR FOR PLAYER 1
        print("PLAYER 1 WINS!")
        print(board)

    elif (board[1, 0] & board[1, 1] & board[1, 2]) == 2:  # IF MIDDLE ROW CLEAR FOR PLAYER 2
        print("PLAYER 2 WINS!")
        print(board)

    elif (board[2, 0] & board[2, 1] & board[2, 2]) == 1:  # IF BOTTOM ROW CLEAR FOR PLAYER 1
        print("PLAYER 1 WINS!")
        print(board)

    elif (board[2, 0] & board[2, 1] & board[2, 2]) == 2:  # IF BOTTOM ROW CLEAR FOR PLAYER 2
        print("PLAYER 2 WINS!")
        print(board)

    elif (board[0, 0] & board[1, 0] & board[2, 0]) == 1:  # IF LEFT COLUMN CLEAR FOR PLAYER 1
        print("PLAYER 1 WINS!")
        print(board)

    elif (board[0, 0] & board[1, 0] & board[2, 0]) == 2:  # IF LEFT COLUMN CLEAR FOR PLAYER 2
        print("PLAYER 2 WINS!")
        print(board)

    elif (board[0, 1] & board[1, 1] & board[2, 1]) == 1:  # IF MIDDLE COLUMN CLEAR FOR PLAYER 1
        print("PLAYER 1 WINS!")
        print(board)

    elif (board[0, 1] & board[1, 1] & board[2, 1]) == 2:  # IF MIDDLE COLUMN CLEAR FOR PLAYER 2
        print("PLAYER 2 WINS!")
        print(board)

    elif (board[0, 2] & board[1, 2] & board[2, 2]) == 1:  # IF RIGHT COLUMN CLEAR FOR PLAYER 1
        print("PLAYER 1 WINS!")
        print(board)

    elif (board[0, 2] & board[1, 2] & board[2, 2]) == 2:  # IF RIGHT COLUMN CLEAR FOR PLAYER 2
        print("PLAYER 2 WINS!")
        print(board)

    elif (board[0, 0] & board[1, 1] & board[2, 2]) == 1:  # IF DIAGONAL (top left to bottom right) CLEAR FOR PLAYER 1
        print("PLAYER 1 WINS!")
        print(board)

    elif (board[0, 0] & board[1, 1] & board[2, 2]) == 2:  # IF DIAGONAL (top left to bottom right) CLEAR FOR PLAYER 2
        print("PLAYER 2 WINS!")
        print(board)

    elif (board[0, 2] & board[1, 1] & board[2, 0]) == 1:  # IF DIAGONAL (top left to bottom right) CLEAR FOR PLAYER 1
        print("PLAYER 1 WINS!")
        print(board)

    elif (board[0, 2] & board[1, 1] & board[2, 0]) == 2:  # IF DIAGONAL (top left to bottom right) CLEAR FOR PLAYER 2
        print("PLAYER 2 WINS!")
        print(board)

    else:  # If win conditions aren't met for either player, calls main function and prints board to continue the game.
        print(board)
        main()


main()  # Call main function.

# Things to fix:
# 1. Clean --> board[((int(player_2_row_move)) - 1), ((int(player_2_column_move)) - 1)]
# 2. Replace conditionals in win_check() with for loops.
# 3. Find out if I can replace all of the if-elif-else statements with something nicer looking and/or more efficient.
# 4. Figure out a way to receive user input for played positions within one statement/variable instead of printing two.
