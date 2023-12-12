#!/usr/bin/env python3

import sys

class Board(object):
    def __init__(self, board, maxX:int, maxY: int, start):
        self.board = board
        self.startX = start[0]
        self.startY = start[1]
        self.maxX = x 
        self.maxY = y

        if self.getNode(self.startX, self.startY-1).getConnection() in ["|", "F", "7"]:
            self.getNode(self.startX, self.startY).addNeighbour((self.startX, self.startY-1))
        if self.getNode(self.startX, self.startY+1).getConnection() in ["|", "L", "J"]:
            self.getNode(self.startX, self.startY).addNeighbour((self.startX, self.startY+1))
        if self.getNode(self.startX-1, self.startY).getConnection() in ["F", "L", "-"]:
            self.getNode(self.startX, self.startY).addNeighbour((self.startX-1, self.startY))
        if self.getNode(self.startX+1, self.startY).getConnection() in ["7", "J", "-"]:
            self.getNode(self.startX, self.startY).addNeighbour((self.startX+1, self.startY))

    def __repr__(self):
        ret = ""
        for y in range(self.maxY):
            for x in range(self.maxX):
                ret = ret+self.board[y][x].getConnection()
            ret += "\n"
        return ret
    def getNode(self, x:int , y:int):
        return self.board[y][x]
    def traverse(self):
        i = 0
        
        nodes = [(self.startX, self.startY)]
        while len(nodes) > 0:
            node_coords = nodes.pop()
            print(f"set {i}, at ({node_coords[0]}, {node_coords[1]})")
            self.getNode(node_coords[0], node_coords[1]).setDistance(i)
            for neighbour in self.getNode(node_coords[0], node_coords[1]).getNeighbours():
                print(f"checking neighbour {neighbour}")
                if self.getNode(neighbour[0], neighbour[1]).getDistance() < 0:
                    nodes.append(neighbour)
            i += 1
        print(f"answer:{(i-1)/2}")
    def cleanBoard(self):
        for y in range(self.maxY):
            for x in range(self.maxX):
                if self.board[y][x].getDistance() < 0:
                    self.board[y][x].setConnection(".")

class Node(object):
    def __init__(self, x: int, y: int, connection: str):
        self.x = x
        self.y = y
        self.connection = connection
        self.distance = -1
        self.neighbours = []
        self.enclosed = False
        match connection:
            case "|":
                self.neighbours.append((self.x, self.y-1))
                self.neighbours.append((self.x, self.y+1))
            case "-":
                self.neighbours.append((self.x-1, self.y))
                self.neighbours.append((self.x+1, self.y))
            case "L":
                self.neighbours.append((self.x, self.y-1))
                self.neighbours.append((self.x+1, self.y))
            case "J":
                self.neighbours.append((self.x, self.y-1))
                self.neighbours.append((self.x-1, self.y))
            case "7":
                self.neighbours.append((self.x-1, self.y))
                self.neighbours.append((self.x, self.y+1))
            case "F":
                self.neighbours.append((self.x+1, self.y))
                self.neighbours.append((self.x, self.y+1))
            case ".":
                print("ground")
            case "S":
                print("start")
            case _:
                print("unknown point")
                exit(-1)
    def getNeighbours(self):
        return self.neighbours
    def addNeighbour(self, coord):
        self.neighbours.append(coord)
    def isVisited(self):
        if self.distance > 0:
            return True
        return False
    def getDistance(self):
        return self.distance
    def setDistance(self, distance: int):
        self.distance = distance
    def getConnection(self):
        return self.connection
    def setConnection(self, conn):
        self.connection = conn
    def setEnclosed(self, enc):
        self.enclosed = enc
    def getEnclosed(self):
        return self.enclosed

x = 0
y = 0
boardArray = []
start = ()
for line in sys.stdin:
    line = line.rstrip()
    row = []
    x = 0
    for c in line:
        if c == "S":
            start = (x, y)
        row.append(Node(x, y, c))
        x+=1
    boardArray.append(row)
    y+=1
board = Board(boardArray, x, y, start)

print(board)
board.traverse()
board.cleanBoard()
print(board)

