#!/usr/bin/env python3

import sys

answer = 0
i=0
card_wins = []
card_count = []
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
  card_wins.append(wc)
  card_count.append(1)

print(f"{card_wins}")

for i in range(len(card_count)):
  print(card_count)
  print(f"card {i+1} has {card_wins[i]} wins and i have {card_count[i]} copies of it, adding {card_count[i]} copies to the next {card_wins[i]} cards")
  for j in range(card_wins[i]):
    if i+j < len(card_wins):
      card_count[i+j+1] = card_count[i+j+1]+card_count[i]
print(card_count)

for c in card_count:
  answer+=c



print(answer)