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
  max_red = 0
  max_blue = 0
  max_green = 0

  game_num = int(game_pattern.search(line).group(1))
  for game in line.split(";"):
    for r in red_pattern.findall(game):
      r = int(r)
      if r > max_red:
        max_red = r
    for b in blue_pattern.findall(game):
      b = int(b)
      if b > max_blue:
        max_blue = b
    for g in green_pattern.findall(game):
      g = int(g)
      if g > max_green:
        max_green = g  
  power = max_red*max_green*max_blue
  print(f"game {game_num} power is {power}")
  
  answer += power


print(answer)
  
  