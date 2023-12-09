#!/usr/bin/env python3

import sys
import math
import re

directions_re = re.compile(r"^[RL]+$")
nodes_re = re.compile(r"^([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)$")

directions = ""
node_map = {}

class MapNode(object):
    def __init__(self, name: str, left: str, right: str):
        self.name = name
        self.left = left
        self.right = right
    def __repr__(self):
        return f"{self.name}->({self.left}, {self.right})"
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left

for line in sys.stdin:
    line = line.rstrip()
    if line == "":
        print("blank line")
    elif directions_re.match(line):
        directions = line
    elif nodes_re.match(line):
        m = nodes_re.match(line)
        node = m.group(1)
        left = m.group(2)
        right = m.group(3)
        if node in node_map:
            print("duplicate node definition found!")
            exit(-1)
        else:
            node_map[node] = MapNode(node, left, right)
        print(f"node: {node}, left: {left}, right: {right}")
    else:
        print("unrecognized line")
        exit(-1)

i = 0
steps = 0
current_node = "AAA"

while current_node != "ZZZ":
    steps += 1
    n = node_map[current_node]
    print(n)
    match directions[i]:
        case "L":
            current_node = node_map[current_node].getLeft()
        case "R":
            current_node = node_map[current_node].getRight()
        case _:
            print("this is impossible")
            exit(-1)
    i = (i+1)%len(directions)

print(steps)