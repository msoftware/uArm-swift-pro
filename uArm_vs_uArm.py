#!/usr/bin/env python3

'''
Eigene Spiele programmieren – Python lernen: Der spielerische Weg zur Programmiersprache
11. September 2017
von Al Sweigart und Volkmar Gronau
Verlag: dpunkt.verlag GmbH (11. September 2017)
Sprache: Deutsch
ISBN-10: 3864904927
ISBN-13: 978-3864904929


Invent Your Own Computer Games with Python16. Dezember 2016
von Al Sweigart
Verlag: No Starch Press; Auflage: 4 (2. Januar 2017)
Sprache: Englisch
ISBN-10: 1593277954
ISBN-13: 978-1593277956
'''

# 'SwiftPro', 'hardware_version': '3.3.0', 'firmware_version': '3.2.0',
# 'api_version': '3.2.0'
# uArm-Python_SDK-2.0

import random
import os
import sys
import time
from time import sleep
from uarm.wrapper import SwiftAPI
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

global swift1
global swift2 

timeout = 200
speed = 35000
uarmStart = False
playerLetter = 'X'
computerLetter = 'O'



swift1 = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})
swift1.waiting_ready() # Computer O
swift2 = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})
swift2.waiting_ready() # Player X




def rahmen(): 
    swift1.flush_cmd()  
    start()
    swift1.set_position(230, 110 , 20, speed = speed,  wait=True, timeout=timeout) 
    swift1.set_position(z = 10) 
    swift1.set_position(230, -110 , 10, speed = speed,  wait=True, timeout=timeout) 
    swift1.set_position(z = 20) 
    swift1.set_position(160, -110 , 20, speed = speed,  wait=True, timeout=timeout) 
    swift1.set_position(z = 10) 
    swift1.set_position(160, 110 , 10, speed = speed,  wait=True, timeout=timeout) 
    swift1.set_position(z = 20) 
    swift1.set_position(110, 40 , 20, speed = speed,  wait=True, timeout=timeout) 
    swift1.set_position(z = 10) 
    swift1.set_position(280, 40, 10, speed = speed, wait=True, timeout=timeout) 
    swift1.set_position(z = 20) 
    swift1.set_position(280, -40 , 20, speed = speed,  wait=True, timeout=timeout) 
    swift1.set_position(z = 10) 
    swift1.set_position(110, -40 , 10, speed = speed,  wait=True, timeout=timeout) 
    swift1.set_position(z = 20) 
    start()

def kasten(x):
    swift1.flush_cmd() 
    swift1.set_position(POS1[x][0], POS1[x][1] , 20, speed = speed,  wait=True, timeout=timeout)
    swift1.set_position(+15, +15 , 0, speed = speed,  relative = True, wait=True, timeout=timeout) 
    swift1.set_position(0, 0 , -10, speed = speed,  relative = True, wait=True, timeout=timeout) 
    swift1.set_position(0, -30 , 0, speed = speed, relative = True, wait=True, timeout=timeout) 
    swift1.set_position(-30, 0 , 0, speed = speed, relative = True, wait=True, timeout=timeout) 
    swift1.set_position(0, +30 , 0, speed = speed, relative = True, wait=True, timeout=timeout) 
    swift1.set_position(+30, 0 , 0, speed = speed, relative = True, wait=True, timeout=timeout) 
    swift1.set_position(0, 0 , +10, speed = speed, relative = True, wait=True, timeout=timeout) 
    swift1.set_position(110, 125,50, speed=speed, relative = False, wait=True, timeout=timeout) 
    swift1.flush_cmd()  
    sleep(0.5)

def kreuz(x):
    swift2.flush_cmd()  
    swift2.set_position(POS2[x][0], POS2[x][1] , 20, speed = speed,  wait=True, timeout=timeout)
    swift2.set_position(+15, +15 , 0, speed = speed,  relative = True, wait=True, timeout=timeout) 
    swift2.set_position(0, 0 , -10, speed = speed,  relative = True, wait=True, timeout=timeout) 
    swift2.set_position(-30, -30 , 0, speed = speed, relative = True, wait=True, timeout=timeout) 
    swift2.set_position(0,0, +10, speed = speed, relative = True, wait=True, timeout=timeout) 
    swift2.set_position(0, +30 , 0, speed = speed, relative = True, wait=True, timeout=timeout) 
    swift2.set_position(0, 0 , -10, speed = speed, relative = True, wait=True, timeout=timeout) 
    swift2.set_position(+30, -30 , 0, speed = speed, relative = True, wait=True, timeout=timeout) 
    swift2.set_position(0, 0 , +10, speed = speed, relative = True, wait=True, timeout=timeout) 
    swift2.set_position(110, 125,50, speed=speed, relative = False, wait=True, timeout=timeout)
    swift2.flush_cmd()  
    sleep(0.5)

POS1 = [(260, 83),  
    (260, 83),  
    (260, -4),   
    (260, -85),  
    (196, 83),   
    (196, -4),   
    (196, -85),  
    (130,83),   
    (130,-4),    
    (130,-85)]

POS2 = [(130,-85),    
    (130,-85),    
    (130,-4),    
    (130,83),   
    (196, -85),  
    (196, -4),   
    (196, 83),   
    (260, -85), 
    (260, -4),   
    (260, 83)]

def start():
    swift1.set_position(110, 135,50, speed=speed,  wait=True, timeout=timeout) # Computer O
    swift2.set_position(110, 135,50, speed=speed,  wait=True, timeout=timeout) # Player X

def drawBoard(board):
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

def whoGoesFirst():
    if random.randint(0, 2): 
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter
   
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or (bo[9] == le and bo[6] == le and bo[3] == le) or (bo[7] == le and bo[5] == le and bo[3] == le) or (bo[9] == le and bo[5] == le and bo[1] == le)) 

def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)
    if len(possibleMoves) != 0:
         return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    for i in range(1, 10):
        copy = getBoardCopy(board)
      
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
   
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
 
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9]) 
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5
    
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])  

def getPlayerMove(board, playerLetter):
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9]) 
    if move != None:
        return move
    if isSpaceFree(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])  

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def tttStart() :
    print('Tic Tac Toe!')
    while True:
        theBoard = [' '] * 10
        turn = whoGoesFirst()
        print('Der ' + turn + ' beginnt.')

        # uArm
        if uarmStart :
            start()
            rahmen()
        #
        gameIsPlaying = True
    
        while gameIsPlaying:
            if turn == 'player':
                move = getPlayerMove(theBoard, playerLetter)
                makeMove(theBoard, playerLetter, move)

                #uArm
                if uarmStart :
                    kreuz(int(move))
                #

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Player hat gewonnen!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        break
                    else:
                        turn = 'computer'
            else:
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                #uArm
                if uarmStart :
                    kasten(int(move))
                 #

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('Computer hat gewonnen!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('Unentschieden!')
                        break
                    else:
                        turn = 'player'
   
        print('Weiter ?(y or n)')
        if not input().lower().startswith('y'):
            break



ans = True
while ans:
    print("""
    1.Tic Tac Toe mit uArm
    2.Tic Tac Toe ohne uArm
    q.Exit/Quit
    """)
    ans = input("Bitte eingeben: ")
    if ans == "1":
      uarmStart = True
      tttStart()
    elif ans == "2":
        tttStart()
    elif ans == "q":
      print("\n Quit") 
      ans = None
    else:
       print("\n .-.. gibt es nicht")









