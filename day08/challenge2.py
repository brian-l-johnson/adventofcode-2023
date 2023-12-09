#!/usr/bin/env python3

import sys
from functools import reduce
import re

directions_re = re.compile(r"^[RL]+$")
nodes_re = re.compile(r"^([A-Z1-9]{3}) = \(([1-9A-Z]{3}), ([1-9A-Z]{3})\)$")

directions = ""
node_map = {}

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

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

a_nodes = []
z_nodes = []

for line in sys.stdin:
    line = line.rstrip()
    if line == "":
        print("blank line")
    elif directions_re.match(line):
        directions = line
    elif nodes_re.match(line):
        m = nodes_re.match(line)
        node = m.group(1)
        if node.endswith("Z"):
            z_nodes.append(node)
        elif node.endswith("A"):
            a_nodes.append(node)
        left = m.group(2)
        right = m.group(3)
        if node in node_map:
            print("duplicate node definition found!")
            exit(-1)
        else:
            node_map[node] = MapNode(node, left, right)
        #print(f"node: {node}, left: {left}, right: {right}")
    else:
        print("unrecognized line")
        exit(-1)

cycles = []

for node in a_nodes:
    i = 0
    steps = 0
    current_node = ""
    while not current_node.endswith("Z"):
        if current_node == "":
            current_node = node
        match directions[i]:
            case "L":
                current_node = node_map[current_node].getLeft()
            case "R":
                current_node = node_map[current_node].getRight()
            case _:
                print("this is impossible")
                exit(-1)
        i = (i+1)%len(directions)
        steps += 1
        if current_node.endswith("Z"):
            print(f"found end node after {steps} steps")
            cycles.append(steps)
        n = node_map[current_node]
        #print(n)
print(lcmm(*cycles))