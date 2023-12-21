#!/usr/bin/env python3

import sys
import math

def isReflection(board):
    if len(board) % 2 == 1:
        return False
    max = len(board)-1
    for i in range(int(len(board)/2)):
        if board[i] != board[max-i]:
            return False
    print(board)
    return True

rows = []
cols = []

ans = 0

for line in sys.stdin:
    line = line.rstrip()
    if line == "":
        print("section ended")
        #make colums list
        for i in range(len(rows[0])):
            cols.append("")
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                cols[j] = cols[j]+rows[i][j]
        print(rows)
        print(cols)
        #find reflections
        for i in range(len(rows)):
            if i!=0 and isReflection(rows[0:i]):
                print(f"rows reflection found 0,{i}")
                ans += int((i+1)/2)*100
            if isReflection(rows[i:len(rows)]):
                ans += int((i+len(rows)+1)/2)*100
                print(f"rows reflection found {i},{len(rows)-1}")

        for i in range(len(cols)):
            if i != 0 and isReflection(cols[0:i]):
                print(f"cols reflection found 0,{i}")
                ans += int((i+1)/2)
            if isReflection(cols[i:len(cols)]):
                ans += int((i+len(cols)+1)/2)
                print(f"cols reflection found {i},{len(cols)-1}")
        
        #reset rows and columns
        rows = []
        cols = []
        print("-------------")
    else:
        rows.append(line)

print(ans)