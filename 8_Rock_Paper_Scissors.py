# Rock/Paper/Scissors

import random

R = 'rock'
S = 'scissors'
P = 'paper'

lst = [R, S, P, R]

print('\n')

print("This is like a typical game of rock, paper, scissors; where you,\
 player 1, are playing against the computer, player 2. Only 'rock', 'paper' \
and 'scissors' are valid inputs.\n")

def win_or_lose(p1: str, p2: str) -> None:

    for i in range(3):
        if p1 == lst[i] and p2 == lst[i + 1]:
            global P1
            P1 = 'W'
        elif p2 == lst[i] and p1 == lst[i + 1]:
            global P2
            P2 = 'W'
            
repeat = 'yes'
   
while repeat == 'yes':
    P1 = 'L'
    P2 = 'L'
    p2 = random.choice(lst)
    while P1 == 'L' and P2 == 'L':
        print('\n', end = '')
        first = input('Player 1: ')
        while first not in lst:
            print('\n', end = '')
            print('Please enter a valid input!')
            print('\n', end = '')
            first = input('Player 1: ')
        win_or_lose(first, p2)
        if P1 == 'L' and P2 == 'L':
            print('\n', end = '')
            print("Player 2 chose {}. It's a draw!".format(p2))
        elif P1 == 'W':
            print('\n', end = '')
            print('Player 2 chose {}. Player 1 wins!'.format(p2))
        elif P2 == 'W':
            print('\n', end = '')
            print('Player 2 chose {}. Player 2 wins!'.format(p2))

        print('\n', end = '')

        repeat = input("Would you like to play again? Please answer\
 'yes' or 'no': ")
    
    answers = ['yes', 'no']
    
    while repeat not in answers :
        print('\n', end = '')
        print('Please enter a valid input!')
        print('\n', end = '')
        repeat = input("Would you like to play again? Please answer \
'yes' or 'no': ")

    print('\n', end = '')

    if repeat == 'no':
        print('Thank you for playing, have a nice day!') 

    