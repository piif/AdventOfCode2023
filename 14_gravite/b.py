#!/bin/env python3

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

map = []
width = None
height = None

def printMap():
    for line in map:
        print(''.join(line))
    print()

def getKey():
    return tuple([ ''.join(line) for line in map ])

def north():
    for x in range(width):
        next = 0
        for y in range(height):
            if map[y][x] == '#':
                next = y+1
            elif map[y][x] == 'O':
                if next != y:
                    map[next][x] = 'O'
                    map[y][x] = '.'
                next += 1

def west():
    for y in range(height):
        next = 0
        for x in range(width):
            if map[y][x] == '#':
                next = x+1
            elif map[y][x] == 'O':
                if next != x:
                    map[y][next] = 'O'
                    map[y][x] = '.'
                next += 1

def south():
    for x in range(width-1, -1, -1):
        next = height-1
        # print("x", x)
        for y in range(height-1, -1, -1):
            # print("y", y, "next", next)
            if map[y][x] == '#':
                next = y-1
            elif map[y][x] == 'O':
                if next != y:
                    map[next][x] = 'O'
                    map[y][x] = '.'
                next -= 1

def east():
    for y in range(height-1, -1, -1):
        next = width-1
        for x in range(width-1, -1, -1):
            if map[y][x] == '#':
                next = x-1
            elif map[y][x] == 'O':
                if next != x:
                    map[y][next] = 'O'
                    map[y][x] = '.'
                next -= 1

def cycle():
    north()
    west()
    south()
    east()
    # printMap()

def weight():
    sum = 0
    for y, line in enumerate(map):
        w = height-y
        sum += w * line.count('O')
    return sum

for y, line in enumerate(open(file)):
    line = line.strip('\n')
    # print("read " + line)
    map.append([ c for c in line ])

width = len(map[0])
height = len(map)

cache = {}
MAX = 1_000_000_000
i = 0
foundLoop = False
while i < MAX:
    cycle()
    k = getKey()
    if k in cache:
        if not foundLoop:
            print("loop", i, cache[k])
            modulo = (MAX - i) % (i - cache[k])
            i = MAX - modulo
            foundLoop = True
    else:
        cache[getKey()] = i
    i += 1

print(weight())
