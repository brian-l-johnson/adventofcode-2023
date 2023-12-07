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

time = ""
distance = ""

for line in sys.stdin:
    line = line.rstrip()
    if time_re.match(line):
        print("fount time line")
        for t in numbers_re.findall(line):
            time = time+t
    elif distance_re.match(line):
        print("found distance")
        for d in numbers_re.findall(line):
            distance = distance+d
    else:
        print("unrecognized line")
        exit(-1)

time = int(time)
distance = int(distance)

print(time)
print(distance)


answer = 1

min = minHold(time, distance)
max = maxHold(time, distance)

if (time-min)*min == distance:
    min = min +1
if (time-max)*max == distance:
    max = max -1

possibilities = max-min+1
print(f"min: {min}, max: {max}, number: {possibilities}")
answer = answer * possibilities;
print(answer)