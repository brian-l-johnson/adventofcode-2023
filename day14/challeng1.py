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

def shiftNorth(board):
    newBoard = copy.deepcopy(board)
    for i in range(1, len(board)):
        for j in range(len(board[i])):
            if newBoard[i][j] == "O":
                newLoc = findFreeNorth(newBoard, i, j)
                newBoard[i][j] = "."
                newBoard[newLoc][j] = "O"
    return newBoard


board = []
for line in sys.stdin:
    line = line.rstrip()
    board.append(list(line))

printBoard(board)
print("==========")
shiftedBoard = shiftNorth(board)

score = scoreBoard(shiftedBoard)
print(score)

