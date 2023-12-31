#!/usr/bin/env python3

import sys
import re

number_re = re.compile(r'^\d$')
hand_def_re = re.compile(r"([AKQJT23456789]){5}\s+\d+")

def makeEffectiveHand(cards):
    if "J" in cards:
        ch = {}
        for c in cards:
            if c in ch:
                ch[c] = ch[c]+1
            else:
                ch[c] = 1
        best = 0
        bestc = "J"
        for k in ch:
            if k != "J":
                if ch[k] > best:
                    best = ch[k]
                    bestc = k
                if ch[k]  == best:
                    s1 = numberify(k)
                    s2 = numberify(bestc)
                    if s1 > s2:
                        best = ch[k]
                        bestc = k
        return cards.replace("J", bestc)
    else:
        return cards
    

def handScore(cards):
    ch = {}
    for c in cards:
        if c in ch:
            ch[c] = ch[c]+1
        else:
            ch[c] = 1
    cards = ch

    if len(cards) == 1: #5 of a kind, best hand
        return 6
    if len(cards) == 2: #either 4 of a kind or full house
        for k in cards:
            if cards[k] == 1 or cards[k] == 4: #four of a kind
                return 5
        return 4 #full house
    if len(cards) == 3: #either two pairs or 3 of a kind
        for k in cards:
            if cards[k] == 3: # 3 of a kind
                return 3
        return 2 #two pairs
    if len(cards) == 4: #pair
        return 1
    return 0 #nothing

def numberify(s: str):
    if(number_re.match(s)):
        return int(s)
    match s:
        case 'A':
            return 14
        case 'K': 
            return 13
        case 'Q':
            return 12
        case 'J':
            return 1
        case 'T':
            return 10
        case _:
            print("illegal character")
            exit(-1)

def breakTie(h1, h2):
    for i in range(len(h1)):
        if numberify(h1[i]) > numberify(h2[i]):
            return True
        if numberify(h1[i]) < numberify(h2[i]):
            return False
    

class Hand(object):
    def __init__(self, cards: str, bid: int):
        self.originalcards = cards
        self.cards = makeEffectiveHand(cards)
        self.bid = int(bid)

    def __repr__(self):
        return f'cards: {self.cards}, bid: {self.bid}'
    def __lt__(self, other):
        selfscore = handScore(self.cards)
        otherscore = handScore(other.cards)
        #print(f"comparing {self.cards} ({selfscore}) to {other.cards} ({otherscore})")
        if selfscore > otherscore:
            #print(f"{self.cards} is better")
            return False
        if selfscore < otherscore:
            #print(f"{other.cards} is better")
            return True
        b =  breakTie(self.originalcards, other.originalcards)
        if b:
            #print(f"{self.cards} is better")
            return False
        else:
            #print(f"{other.cards} is better")
            return True
    def getBid(self):
        return self.bid
    def getCards(self):
        return self.cards
    def getOriginalCards(self):
        return self.originalcards
    

hands = []
for line in sys.stdin:
    line = line.rstrip()
    if not hand_def_re.match(line):
        print(f"unparsable line: {line}")
        exit(-1)
    hand_def = line.split(" ")
    hands.append(Hand(hand_def[0], hand_def[1]))

print(hands)
hands.sort()
print(hands)

answer = 0
for i in range(len(hands)):
    answer = answer + hands[i].getBid() * (i+1)
    cards = hands[i].getCards()
    print(f"{cards}:{hands[i].getOriginalCards()}:{hands[i].getBid()}:{handScore(cards)}:{numberify(cards[0])}:{numberify(cards[1])}:{numberify(cards[2])}:{numberify(cards[3])}:{numberify(cards[4])}")

print(answer)


