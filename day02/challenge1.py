#!/usr/bin/env python3

import sys
import re

sum = 0

game_pattern = re.compile(r'^Game (\d+):')
red_pattern = re.compile(r'(\d+) red')
blue_pattern = re.compile(r'(\d+) blue')
green_pattern = re.compile(r'(\d+) green')

answer = 0

for line in sys.stdin:
  line = line.rstrip()
  possible = True
  game_num = int(game_pattern.search(line).group(1))
  for game in line.split(";"):
    red_total = 0
    for r in red_pattern.findall(game):
      red_total = red_total + int(r)
    blue_total = 0
    for b in blue_pattern.findall(game):
      blue_total = blue_total + int(b)
    green_total = 0
    for g in green_pattern.findall(game):
      green_total = green_total + int(g)
  

    if red_total > 12 or green_total > 13 or blue_total > 14:
      possible = False
  if possible:
    answer+=game_num

print(answer)
  
  