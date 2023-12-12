#!/usr/bin/env python3

import sys
import copy
import math

board = []

cols = 0
rows = 0

for line in sys.stdin:
    line = line.rstrip()
    row = []
    cols = 0 
    for c in line:
        cols+=1
        row.append(c)
    board.append(row)
    if "#" not in row:
        board.append(copy.deepcopy(row))
        rows+=1
    rows+=1

#cols -= 1

print(f"rows: {rows}, cols: {cols}")

print(board)
emptyCols = []
for c in range(cols):
    emptyCol = True
    for r in range(rows):
        print(f"checking ({c},{r})")
        if board[r][c] == "#":
            emptyCol = False
    if emptyCol:
        emptyCols.append(c)

print(board)


count = 0
for c in emptyCols:
    print(f"colume {c} is empty")
    for r in range(rows):
        board[r].insert(c+count, '.')
    count+=1
cols +=count
print(board)


galaxies = []
for r in range(rows):
  for c in range(cols):
      if board[r][c] == "#":
          galaxies.append((r,c))

print(galaxies)


ans = 0
while len(galaxies) > 0:
    g = galaxies.pop()
    for gc in galaxies:
        print(f"comparing {g} to {gc}")
        d = abs(g[0]-gc[0])+abs(g[1]-gc[1])
        ans += d
print(ans)