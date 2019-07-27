# Tic-Tac-Toe
# Made by: Atishay Jain
# I took the idea from the book "Invent Your Own Computer Games with Python"

import random
from os import name,system
from time import sleep

def clear() :
    # This function clears the screen.
    if name == 'nt' :
        _ = system('cls')
    else :
        _ = system('clear')

def draw_board(board) :
    # This function prints the "board".
    # "board" is a list of 10 elements representing the game_board (ignoring index 0).
    print()
    print( ' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] )
    print('---|---|---')
    print( ' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] )
    print('---|---|---')
    print( ' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] )
    print()

def letter_choice() :
    # This function lets the player to select the letter he wants.
    # The player can choose to be X or O.
    # This function returns the player's character.
    letter = ''
    while letter != 'X' and letter != 'O' :
        print("Do you want to be X or O ?",end = ' ')
        letter = input().upper()
    return letter

def first_chance() :
    # This function decides wheter player or computer will have the first chance.
    num = random.randint(1,2)
    if num == 1 :
        return 'player'
    else :
        return 'computer'

def is_winner(board, letter) :
    # This function returns true if the player has won.
    return (
    (board[7] == board[8] == board[9] == letter) or
    (board[4] == board[5] == board[6] == letter) or
    (board[1] == board[2] == board[3] == letter) or
    (board[7] == board[4] == board[1] == letter) or
    (board[8] == board[5] == board[2] == letter) or
    (board[9] == board[6] == board[3] == letter) or
    (board[1] == board[5] == board[9] == letter) or
    (board[7] == board[5] == board[3] == letter)
    )

def is_space_free(board, position) :
    # Returns True if the passed position is blank on the passed board.
    return board[position] == ' '

def player_move(board) :
    # Gets the player's move.
    move = input("Enter your move : ")
    while not (move in '1 2 3 4 5 6 7 8 9'.split(' ') and is_space_free(board, int(move))) :
        move = input("Enter a valid move : ")
    return int(move)

def choose_random_move(board, moves_list) :
    # Chooses a random valid move from the passed moves_list.
    possible_moves = []
    for i in moves_list :
        if is_space_free(board, i) :
            possible_moves.append(i)
    if len(possible_moves) == 0 :
        return None
    else :
        return random.choice(possible_moves)

def get_computer_move(board, computer_letter) :
    # This function returs the computer's next move for passed board.
    if computer_letter == 'O' :
        player_letter = 'X'
    else :
        player_letter = 'O'

    # Algorithm for game's AI :
    # First, check if computer can win in one move.
    for i in range(1,10) :
        if is_space_free(board, i) :
            board_copy = board.copy()
            board_copy[i] = computer_letter
            if is_winner(board_copy, computer_letter) :
                return i

    # Next, check if the player can win in one move.
    for i in range(1,10) :
        if is_space_free(board, i) :
            board_copy = board.copy()
            board_copy[i] = player_letter
            if is_winner(board_copy, player_letter) :
                return i

    # Try to take the corners if they are free.
    corners = [1,3,7,9]
    move = choose_random_move(board, corners)
    if move != None :
        return move

    # Take the centre if it is free.
    if is_space_free(board, 5) :
        return 5

    # Choose one of the remaining moves.
    remaining = [2,4,6,8]
    move = choose_random_move(board, remaining)
    return move

def is_board_full(board) :
    # Returns True if the board is full, else return False.
    for i in range(1,10) :
        if is_space_free(board, i) :
            return False
    return True

def play_again() :
    # Returns true if the payer has decided to play again.
    player_choice = input('Do you want to play again(Yes/No)? ')
    if player_choice.lower().startswith('y') :
        return True

def play_with_computer() :
    # fuction for runnig game in 1P mode
    board = [' ']*10

    player_letter = letter_choice()
    if player_letter == 'O' :
        computer_letter = 'X'
    else :
        computer_letter = 'O'

    chance = first_chance()
    if chance == 'computer' :
        print("Computer goes first!\n")
    else :
        print("You go first!\n")

    playing = True
    while playing :
        if is_board_full(board) :
            print('The game has tied.')
            playing = False
            break

        if chance == 'computer' :
            move = get_computer_move(board, computer_letter)
            print('Computer\'s turn : ')
            board[move] = computer_letter
            chance = 'player'
            sleep(0.7)
        elif chance == 'player' :
            move = player_move(board)
            board[int(move)] = player_letter
            chance = 'computer'
            sleep(0.3)
        draw_board(board)

        if is_winner(board, computer_letter) :
            print('Computer has won!\n')
            playing = False
        elif is_winner(board, player_letter) :
            print('Congratulations! You won\n')
            playing = False

def play_with_human() :
    # Function for running game in 2P mode.
    board = [' ']*10

    player1 = input("Player 1 choose X or O : ")
    while player1.upper() not in 'XO' :
        player1 = input("Enter a valid character : ")
    player1 = player1.upper()
    if player1 == 'X' :
        player2 = 'O'
    else :
        player2 = 'X'
    print(player2, 'is Player 2\n')

    chance = random.randint(1,2)
    if chance == 1 :
        print("Player 1 goes first.\n")
    else :
        print("Player 2 goes first.\n")

    playing = True
    while playing :
        if is_board_full(board) :
            print("The game has tied")
            playing = False
            break

        if chance == 1 :
            player = player1
            print("Player 1's turn :")
            chance = 2
        else :
            player = player2
            print("Player 2's turn :")
            chance = 1
        move = player_move(board)

        board[move] = player
        sleep(0.3)
        draw_board(board)

        if is_winner(board, player) :
            if player == player1 :
                print("Congratulations! Player 1 has won")
            else :
                print("Congratulations! Player 2 has won")
            playing = False

def main() :
    clear()
    print("Welcome to Tic-Tac-Toe!\n")

    game_type = input("1P or 2P : ")
    while not (game_type.startswith('1') or game_type.startswith('2')) :
        game_type = input("Enter a valid choice : ")
    if game_type.startswith('1') :
        play_with_computer()
    else :
        play_with_human()

    if play_again() == True :
        main()

if __name__ == '__main__' :
    main()
