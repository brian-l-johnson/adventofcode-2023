#!/usr/bin/env python3

import sys

answer = 0
i=0
for line in sys.stdin:
  i+=1
  line = line.rstrip()
  card = line.split("|")
  winners = card[0].split(":")[1].split(" ")
  numbers = card[1].split(" ")
  wc = 0
  print(f"winning numbers: {winners}")
  print(f"card: {numbers}")
  for winner in winners:
    if winner != '' and winner in numbers:
      wc += 1
  if wc > 0:
    score = 2**(wc-1)
    answer+=score
    print(f"there were {wc} winers on card {i} for a score of {score}")
print(answer)