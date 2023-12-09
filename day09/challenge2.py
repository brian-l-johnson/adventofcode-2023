#!/usr/bin/env python3

import sys

def allZero(list):
    return all(i == 0 for i in list)

answer = 0

def predict(arr):
    arr.reverse()
    while len(arr) > 1:
        arr[1] = arr[1]- arr[0]
        arr = arr[1:]
    return arr[0]

for line in sys.stdin:
    line = line.rstrip()
    sequence = line.split(" ")
    sequence = [int(i) for i in sequence]
    firstValues = []
    
    searching = True
    print(sequence)
    while searching:
        diff = []
        for i in range(len(sequence)-1):
            diff.append(sequence[i+1]-sequence[i])
        print(diff)
        firstValues.append(sequence[0])
        if(allZero(diff)):
            searching = False
            firstValues.append(0)
        else:
            sequence = diff
    print(f"first value in each: {firstValues}")
    prediction = predict(firstValues)
    print(prediction)
    answer+=prediction
print(answer)
            