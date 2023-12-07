#!/usr/bin/env python3

import sys
import math
import re

def minHold(t, d):
    mt = .5*(t - math.sqrt(t*t - 4*d))
    return math.ceil(mt)
def maxHold(t,d):
    mt = .5*(math.sqrt(t*t-4*d)+t)
    return math.floor(mt)

time_re = re.compile("^Time:\s+((\d+)+\s*)+$")
distance_re = re.compile("Distance:\s+((\d+)+\s*)+$")
numbers_re = re.compile("(\d+)\s*")

times = []
distances = []

for line in sys.stdin:
    line = line.rstrip()
    if time_re.match(line):
        print("fount time line")
        for t in numbers_re.findall(line):
            times.append(int(t))
    elif distance_re.match(line):
        print("found distance")
        for d in numbers_re.findall(line):
            distances.append(int(d))
    else:
        print("unrecognized line")
        exit(-1)

if len(times) != len(distances):
    print("time and distance definition mismatch")
    exit(-1)

print(times)
print(distances)


answer = 1

for i in range(len(times)):
    min = minHold(times[i], distances[i])
    max = maxHold(times[i], distances[i])

    if (times[i]-min)*min == distances[i]:
        min = min +1
    if (times[i]-max)*max == distances[i]:
        max = max -1

    possibilities = max-min+1
    print(f"min: {min}, max: {max}, number: {possibilities}")
    answer = answer * possibilities;
print(answer)