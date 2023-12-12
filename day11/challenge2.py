#!/usr/bin/env python3

import sys
import copy

rowset = set()
colset = set()
galaxies = []

row = 0
for line in sys.stdin:
    line = line.rstrip()
    col = 0
    for c in line:
        if c == "#":
            rowset.add(row)
            colset.add(col)
            galaxies.append((row, col))
        col+=1
    row+=1


og = copy.deepcopy(galaxies)
print(rowset)
print(colset)
print(max(rowset))
print(max(colset))
print(galaxies)

offset = 999999

for r in range(max(rowset)):
    if r not in rowset:
        for i in range(len(og)):
            if og[i][0] > r:
                galaxies[i] = (galaxies[i][0]+offset, galaxies[i][1])
for c in range(max(colset)):
    if c not in colset:
        for i in range(len(og)):
            if og[i][1] > c:
                galaxies[i] = (galaxies[i][0], galaxies[i][1]+offset)

ans = 0
while len(galaxies) > 0:
    g = galaxies.pop()
    for gc in galaxies:
        print(f"comparing {g} to {gc}")
        d = abs(g[0]-gc[0])+abs(g[1]-gc[1])
        ans += d
print(ans)
