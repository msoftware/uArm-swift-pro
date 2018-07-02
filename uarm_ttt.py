#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Eigene Spiele programmieren – Python lernen: Der spielerische Weg zur Programmiersprache
#11. September 2017
#von Al Sweigart und Volkmar Gronau
#Verlag: dpunkt.verlag GmbH (11. September 2017)
#Sprache: Deutsch
#ISBN-10: 3864904927
#ISBN-13: 978-3864904929

#Invent Your Own Computer Games with Python16. Dezember 2016
#von Al Sweigart
#Verlag: No Starch Press; Auflage: 4 (2. Januar 2017)
#Sprache: Englisch
#ISBN-10: 1593277954
#ISBN-13: 978-1593277956

import random

# uArm
import sys
import os
from time import sleep
from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
swift = SwiftAPI() # {'hwid': 'USB VID:PID=2341:0042'}
sleep(2)

xst = 290 # startpunkt
yst = 120

auf = 20
ab = 10
spidy = 35000

def senken():
    swift.set_position(z = ab, speed = spidy, wait = True) 
def heben():
    swift.set_position(z = auf, speed = spidy, wait = True)      
def rahmen(): 
    swift.flush_cmd()  
    start()
    # reihe
    swift.set_position(xst - 60, yst , auf, speed = spidy,  wait = True) 
    senken()
    swift.set_position(0, -260 , 0, speed = spidy, relative = True, wait = True) 
    heben()
    swift.set_position(-60, 0 , 0, speed = spidy, relative = True, wait = True) 
    senken()
    swift.set_position(0, +260 , 0, speed = spidy, relative = True, wait = True) 
    heben()
    #ausgang
    swift.set_position(xst, yst , auf, speed = spidy,  wait = True) 
    #spalte 1
    swift.set_position(0, -85 , 0, speed = spidy, relative = True, wait = True) 
    senken()
    swift.set_position(-170, 0 , 0, speed = spidy, relative = True, wait = True) 
    heben()
    #spalte 2
    swift.set_position(0, -90 , 0, speed = spidy, relative = True, wait = True) 
    senken()
    swift.set_position(+170, 0 , 0, speed = spidy, relative = True, wait = True) 
    heben()
POS = [
        (xst - 25, yst - 40),  #0 gleich 1
        (xst - 25, yst - 40),  # 1
        (xst - 25, yst - 130), # 2
        (xst - 25, yst - 220), # 3
        (xst - 90, yst - 40),  # 4
        (xst - 90, yst - 130), # 5
        (xst - 90, yst - 220), # 6
        (xst - 145,yst - 40),  # 7
        (xst - 145,yst - 130), # 8
        (xst - 145,yst - 220)  # 9
        ]
def start():
    swift.set_position(150, 0, auf + 30, speed = spidy,  wait = True) 
    swift.flush_cmd()  
    sleep(1)

def kasten(x):
    swift.flush_cmd() 
    swift.set_position(POS[x][0], POS[x][1] , auf, speed = spidy,  wait = True)
    #1
    swift.set_position(+15, +15 , 0, speed = spidy,  relative = True, wait = True) 
    senken()
    #2
    swift.set_position(0, -30 , 0, speed = spidy, relative = True, wait = True) 
    #3
    swift.set_position(-30, 0 , 0, speed = spidy, relative = True, wait = True) 
    #4
    swift.set_position(0, +30 , 0, speed = spidy, relative = True, wait = True) 
    #1
    swift.set_position(+30, 0 , 0, speed = spidy, relative = True, wait = True) 
    heben()

def kreuz(x):
    swift.flush_cmd()  
    swift.set_position(POS[x][0], POS[x][1] , auf, speed = spidy,  wait = True)
    #1
    swift.set_position(+15, +15 , 0, speed = spidy,  relative = True, wait = True) 
    senken()
    # zu 3
    swift.set_position(-30, -30 , 0, speed = spidy, relative = True, wait = True) 
    heben()
    # zu 4
    swift.set_position(0, +30 , 0, speed = spidy, relative = True, wait = True) 
    senken()
    # zu 2
    swift.set_position(+30, -30 , 0, speed = spidy, relative = True, wait = True) 
    heben()

# ende Uarm


def drawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def inputPlayerLetter():
# Lets the player type which letter they want to be.
# Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
        # the first element in the list is the player’s letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 2): 
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')

def makeMove(board, letter, move):
    board[move] = letter
    
def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    # uArm
    if computerLetter == 'X' :
        kasten(int(move))
    else:
        kreuz(int(move))
    #
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)
    if len(possibleMoves) != 0:
         return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move

    for i in range(1, 10):
        copy = getBoardCopy(board)
      

        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
               return i
           

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
               return i
    
    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9]) 
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5
    
    # Move on one of the sides.
        return chooseRandomMoveFromList(board, [2, 4, 6, 8])  


def isBoardFull(board):
# Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    # uArm
    start()
    rahmen()
    #
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player’s turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    break
                else:
                    turn = 'computer'

        else:
            # Computer’s turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            # uArm
            if computerLetter == 'X' :
                kreuz(int(move))
            else:
                kasten(int(move))
            #
                       
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                # uArm
                swift.set_buzzer()
                start()
                #
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break


