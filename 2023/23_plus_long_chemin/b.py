#!/bin/env python3

import sys
sys.setrecursionlimit(5000)

# file = 'sample_a.txt'
file = 'data_a.txt'

map = []

def readMap():
    global map
    for y, line in enumerate(open(file)):
        line = line.strip('\n')
        # print("read " + line)
        l = []
        for x, c in enumerate(line):
            l.append(c!='#')
        map.append(l)

def printMap():
    for line in map:
        for plot in line:
            print(' ' if plot else '#', end='')
        print()

def addArc(x0, y0, x, y, weight):
    if (x0, y0) in graph:
        if (x, y) not in graph[(x0, y0)]:
            graph[(x0, y0)][(x, y)] = weight
            return True
        else:
            return False
    else:
        graph[(x0, y0)] = { (x, y): weight }
        return True

def createGraph():
    edges = [ ( None, None, start[0], start[1] ) ]
    while len(edges) != 0:
        # print("try", edges)
        newEdges = []
        for (x0, y0, x, y) in edges:
            # print("from", x0, y0, x, y)
            weight = 1 if x0 is not None else 0
            prev = (x0, y0)
            while True: # find longest arc
                neighbours = []
                for (nx, ny) in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                    if (nx, ny) == prev:
                        continue
                    if nx not in range(width) or ny not in range(height):
                        continue
                    if not map[ny][nx]:
                        continue
                    # print("  neighbour", nx, ny)
                    neighbours.append((nx, ny))
                if len(neighbours) != 1:
                    print("  fork", neighbours)
                    break
                weight += 1
                prev = (x, y)
                (x, y) = neighbours[0]

            if len(neighbours) > 1:
                newArc = addArc(x0, y0, x, y, weight)
                if newArc:
                    if x0 is not None:
                        addArc(x, y, x0, y0, weight)
                    for (nx, ny) in neighbours:
                        if (x, y, nx, ny) not in newEdges:
                            newEdges.append((x, y, nx, ny))
            elif (x, y) == end:
                newArc = addArc(x0, y0, x, y, weight)

        edges = newEdges

def printGraph():
    for node,edges in graph.items():
        print(node, edges)

def printPath(path, always = False):
    global longest
    prev = path[0]
    sum = 0
    s = ''
    for p in path[1:]:
        w = graph[prev][p]
        s += f'-{w}-> {p} '
        prev = p
        sum += w
    if always or sum > longest:
        longest = sum
        print(s + f' => {sum}')

def findLongest(node, path=[], indent=0):
    # print(indent*'  ', "try", node, path)
    if node == end:
        printPath(path + [ end ])
        return 0
    maxLen = 0
    for edge,w in graph[node].items():
        if edge not in path:
            maxLen = max(maxLen, findLongest(edge, path + [ node ])+w , indent+1)
    # if maxLen == 0:
    #     print("Dead end from", node, ": ", end='')
    #     printPath(path, True)
    return maxLen

readMap()

width = len(map[0])
height = len(map)

start = (map[0].index(True), 0)
end = (map[-1].index(True), height-1)

# printMap()
print(f'size {width}x{height}, from {start} to {end}')

graph = {}
createGraph()
printGraph()
longest = 0
l = findLongest((None, None))
print(l)