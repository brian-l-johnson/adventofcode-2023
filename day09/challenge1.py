#!/usr/bin/env python3

import sys

def allZero(list):
    return all(i == 0 for i in list)

answer = 0

for line in sys.stdin:
    line = line.rstrip()
    sequence = line.split(" ")
    sequence = [int(i) for i in sequence]
    lastValues = []
    
    searching = True
    print(sequence)
    while searching:
        diff = []
        for i in range(len(sequence)-1):
            diff.append(sequence[i+1]-sequence[i])
        print(diff)
        lastValues.append(sequence[-1])
        if(allZero(diff)):
            searching = False
        else:
            sequence = diff
    print(f"last value in each: {lastValues}")
    prediction = sum(lastValues)
    print(prediction)
    answer+=prediction
print(answer)
            