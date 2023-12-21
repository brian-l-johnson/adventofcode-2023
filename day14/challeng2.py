#!/usr/bin/env python3

import sys
import copy

def printBoard(board):
    for line in board:
        print("".join(line))

def scoreBoard(board):
    score = 0
    boardlen = len(board)
    for i in range(len(board)):
        lc = 0
        for s in board[i]:
            if s == "O":
                lc+=1
        score+=(lc*(boardlen-i))
    return score

def findFreeNorth(board, r:int,c:int):
    blocked = False
    while not blocked:
        if r == 0:
            blocked = True
        elif board[r-1][c] != '.':
            blocked = True
        else:
            r-=1
    return r

def findFreeSouth(board, r:int, c:int):
    blocked = False
    max = len(board)
    while not blocked:
        if r == max-1:
            blocked = True
        elif board[r+1][c] != '.':
            blocked = True
        else:
            r+=1
    return r


def findFreeEast(board, r:int, c:int):
    blocked = False
    maxCol = len(board[0])
    while not blocked:
        if c == maxCol-1:
            blocked = True
        elif board[r][c+1] != '.':
            blocked = True
        else:
            c+=1
    return c

def findFreeWest(board, r:int, c:int):
    blocked = False
    while not blocked:
        if c == 0:
            blocked = True
        elif board[r][c-1] != '.':
            blocked = True
        else:
            c-=1
    return c

def shiftNorth(board):
    newBoard = copy.deepcopy(board)
    for i in range(1, len(board)):
        for j in range(len(board[i])):
            if newBoard[i][j] == "O":
                newLoc = findFreeNorth(newBoard, i, j)
                newBoard[i][j] = "."
                newBoard[newLoc][j] = "O"
    return newBoard

def shiftEast(board):
    newBoard = copy.deepcopy(board)
    for i in range(len(newBoard)):
        for j in reversed(range(len(board[i]))):
            if newBoard[i][j] == "O":
                newLoc = findFreeEast(newBoard, i, j)
                newBoard[i][j] = '.'
                newBoard[i][newLoc] = "O"
    return newBoard

def shiftWest(board):
    newBoard = copy.deepcopy(board)
    for i in range(len(newBoard)):
        for j in range(len(board[i])):
            if newBoard[i][j] == "O":
                newLoc = findFreeWest(newBoard, i, j)
                newBoard[i][j] = '.'
                newBoard[i][newLoc] = "O"
    return newBoard

def shiftSouth(board):
    newBoard = copy.deepcopy(board)
    for i in reversed(range(len(board))):
        for j in range(len(board[i])):
            if newBoard[i][j] == "O":
                newLoc = findFreeSouth(newBoard, i, j)
                newBoard[i][j] = "."
                newBoard[newLoc][j] = "O"
    return newBoard

board = []
for line in sys.stdin:
    line = line.rstrip()
    board.append(list(line))

printBoard(board)
#score = 0
for i in range(1021):
    board = shiftNorth(board)
    board = shiftWest(board)
    board = shiftSouth(board)
    board = shiftEast(board)
    #score+=scoreBoard(board)
    #print(f"{i}: {score}")
    #if i%10000 == 0:
    #    print(f"{i}")
    print(f"{i}: {scoreBoard(board)}")
print("=========")
#printBoard(board)


#score = scoreBoard(shiftedBoard)
#print(score)

