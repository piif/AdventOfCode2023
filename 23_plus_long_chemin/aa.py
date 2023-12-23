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
        print("read " + line)
        l = []
        for x, c in enumerate(line):
            l.append((c, None, False)) # (kind, longest distance, on my current search path)
        map.append(l)

def printMap():
    for line in map:
        for (kind, dist, current) in line:
            if dist is not None:
                d = f'{dist:3}'
            else:
                d = f'   '
            print(f'{d}{kind}', end='')
        print()

def tryMove(step, x, y, nx, ny, indent):
    if (nx, ny) == end:
        map[ny][nx] = ('.', step, False)
        print("Found", step)
        # print(indent*'  ', "Found", step)
        return step
    if nx not in range(width) or ny not in range(height):
        return FAR_AWAY
    (kind, distance, current) = map[ny][nx]
    if kind == '#':
        return FAR_AWAY
    if current:
        # back on my own path
        return FAR_AWAY
    if distance is None or distance < step:
        # new or longer path, continue to explore
        map[ny][nx] = (kind, step, True)
        result = findLongestPath(step+1, nx, ny, indent)
        if result <= step or result == FAR_AWAY:
            map[ny][nx] = (kind, None, False)
        else:
            map[ny][nx] = (kind, step, False)
        return result
        
    return FAR_AWAY # already found a longer path

def findLongestPath(step, x, y, indent=0):
    (kind, distance, current) = map[y][x]
    # print(indent*'  ', "findLongestPath", step, x, y)

    maxDistance = -1
    if kind in '.<':
        result = tryMove(step, x, y, x-1, y, indent+1)
        # print(indent*'  ', " < ", result)
        if result != FAR_AWAY and result >= step:
            maxDistance = max(maxDistance, result)
    if kind in '.>':
        result = tryMove(step, x, y, x+1, y, indent+1)
        # print(indent*'  ', " > ", result)
        if result != FAR_AWAY and result >= step:
            maxDistance = max(maxDistance, result)
    if kind in '.^':
        result = tryMove(step, x, y, x, y-1, indent+1)
        # print(indent*'  ', " ^ ", result)
        if result != FAR_AWAY and result >= step:
            maxDistance = max(maxDistance, result)
    if kind in '.v':
        result = tryMove(step, x, y, x, y+1, indent+1)
        # print(indent*'  ', " v ", result)
        if result != FAR_AWAY and result >= step:
            maxDistance = max(maxDistance, result)

    # print(indent*'  ', "->", maxDistance)
    return FAR_AWAY if maxDistance == -1 else maxDistance


readMap()

width = len(map[0])
height = len(map)
FAR_AWAY = width * height
start = (map[0].index(('.', None, False)), 0)
map[0][start[0]] = ('.', 0, False)
end = (map[-1].index(('.', None, False)), height-1)

printMap()
print(f'size {width}x{height}, from {start} to {end}')

r = findLongestPath(1, *start)
printMap()
print(r)
