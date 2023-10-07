#!/usr/bin/env python

from IPython.display import clear_output

def display_board(board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']):
    
    horse = board
    # for _ in range(9):
    #     horse.append(' ')
    # # print (horses)

    for i in range(3):
        print (horse[7-1-i*3],'|',horse[8-1-i*3],'|',horse[9-1-i*3])
        if i != 2:
            print ("-","|","-","|",'-')

def player_input():
    player1 = "not X nor O"
    while player1 not in ['X', 'O']:
        player1 = input('Choose your player1 between "X" and "O": ')
        if player1 not in ['X', 'O']:
            clear_output()
            print ('I said, choose a player between "X" and "O"!: ')
    clear_output()
    print('player1 chose', player1)
    player2 = ''
    if ['X','O'].index(player1) == 0:
        player2 = 'O'
    else:
        player2 = 'X'
    print('player2 is then ', player2)
    return player1, player2


def place_marker(board, marker, position):

    board[position-1] = marker
    # return board


def win_check(board, mark):
    
    for i in range(3):
        if mark == board[9-1-i*3] and mark == board[8-1-i*3] and mark == board[7-1-i*3]:
            return True
        if mark == board[9-1-i] and mark == board[6-1-i] and mark == board[3-1-i]:        
            return True
    if mark == board[9-1] and mark == board[5-1] and mark == board[1-1]:
        return True
    if mark == board[7-1] and mark == board[5-1] and mark == board[3-1]:
        return True    

import random

def choose_first():
    randout = random.randint(0,1)
    if randout == 0:
        print ('Player 1 goes first')
        return 0
    if randout != 0:
        print ('Player 2 goes first')        
        return 1

def space_check(board, position):

    if board[position-1] != ' ':
        # print('Already filled! Choose another position!')
        return False
    else:
        return True

def full_board_check(board):
    
    if ' ' not in board:
        return True
    else:
        return False

def player_choice(board):
    
    position = 'wrong position'
    space_checker = False
    while space_checker == False:
        position = input('Where do you want to put your horse? give me an integer between 1 to 9: ')
        if position.isdigit() == False:
            # clear_output()
            print("It's not even an integer you moron!")
            continue
        # else:
    #     while position not in range(1,10):
        if int(position) not in range(1,10):
            # clear_output()
            print("Betweeeen 1 and 9")
            continue
        if space_check(board, int(position)) == False:
            clear_output()
            print("Sorry, this position is already filled")
            display_board(board)
        else:
            space_checker=True
    
    clear_output()
    return int(position)

def replay():
    yesno = 'not y nor n'    
    while yesno not in ['y', 'n']:
        yesno = input('Wanna play one more time? [y/n] ')
        if yesno not in ['y', 'n']:
            # clear_output()
            print('Say it between "y" or "n"')
        elif yesno == 'y':
            return True
        elif yesno == 'n':
            return False

print('Welcome to Tic Tac Toe')
continue_game = True
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display_board(board)
player1, player2 = player_input()
first_player_int = choose_first()
p1 = '' # first player
p1_int = -1
p2 = '' # second player
p2_int = -1
if first_player_int == 0:
    p1 = player1
    p2 = player2
    p1_int = 1
    p2_int = 2
else:
    p1 = player2
    p2 = player1
    p1_int = 2
    p2_int = 1

game_on = True
display_board(board)
while continue_game:
    # display_board(board)
    while game_on:
        
        
        #Player 1 Turn
        print(f'Player{p1_int}, ')
        position = player_choice(board)

        place_marker(board, p1, position)
        clear_output()
        display_board(board)

        if full_board_check(board) == True:
            game_on = False
            print('Space Full! Game Over!!')
            break
        if win_check(board, p1) == True:
            game_on = False
            print(f'Player{p1_int} Won!')
            break
        elif win_check(board, p2) == True:
            game_on = False
            print(f'Player{p2_int} Won!')
            break
            
        # Player2's turn.
        print(f'Player{p2_int}, ')
        position = player_choice(board)
        place_marker(board, p2, position)
        clear_output()
        display_board(board)

        if full_board_check(board) == True:
            game_on = False
            print('Space Full! Game Over!!')
            break
            
            #pass
        if win_check(board, p1) == True:
            game_on = False
            print(f'Player{p1_int} Won!')
            break
        elif win_check(board, p2) == True:
            game_on = False
            print(f'Player{p2_int} Won!')
            break

    if not replay():
        display_board(board)
        continue_game = False
        break
    else:
        game_on = True
        board = [' ' for i in range(9)]

