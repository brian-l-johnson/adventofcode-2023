#!/usr/bin/env python3

import sys
import re

numbers = []
symbols = []
ln = 0

answer = 0

def pointAdjacent(a, b):
  if abs(a[0]-b[0]) <= 1 and abs(a[1]-b[1]) <= 1:
    return True
  return False

def rangeAdjacent(locs, p):
  for l in locs:
    if pointAdjacent(l,p):
      return True
  return False

def numberNextToSymbol(nlocs, slocs):
  for sl in slocs:
    if rangeAdjacent(nlocs, sl):
      return True
  return False
  

for line in sys.stdin:
  #line = line.rstrip()
  n = ""
  n_loc = []
  for i in range(len(line)):
    if re.match(r"\d", line[i]): #digit
      n += line[i]
      n_loc.append((ln,i))
    else:
      if len(n) > 0:
        numbers.append((int(n), n_loc))
        n = ""
        n_loc = []
      if line[i] != '.' and line[i] != "\n": #if you are not a number or a . you are a symbol
        symbols.append((ln,i))
  ln+=1

print(f"there are {len(numbers)} numbers and {len(symbols)} symbols")

for nt in numbers:
  n = nt[0]
  locs = nt[1]
  if numberNextToSymbol(locs, symbols):
    #print(f"{n} is adjacent to a symbol")
    answer += n
  else:
    print(f"{n} is not adjacent to any symbols: {locs}")

print(answer)
