#!/bin/env python3
import re

sum = 0

# file = 'sample_a.txt'  # 24 in , 38 wall , 8 out
# file = 'sample_aa.txt'
file = 'data_a.txt' # 31579 in , 2750 wall , 34329 in+wall , 65631 out ?

def readMap():
    commands = []
    for i, line in enumerate(open(file)):
        line = line.strip('\n')
        (dir, steps, r, g, b) = re.match('(.) (\d+) \(#(..)(..)(..)\)', line).groups()
        commands.append((dir, int(steps), (int(r, 16), int(g, 16), int(b, 16))))

    x = 0
    y = 0
    xList = [ ]
    yList = [ ]
    cList = [ ]

    for (dir, steps, color) in commands:
        for i in range(steps):
            # print(dir, x, y, color)
            xList.append(x)
            yList.append(y)
            cList.append(color)
            if dir == 'R':
                x += 1
            elif dir == 'L':
                x -= 1
            elif dir == 'D':
                y += 1
            elif dir == 'U':
                y -= 1

    minX = min(xList)
    maxX = max(xList)
    minY = min(yList)
    maxY = max(yList)

    print(minX, maxX, minY, maxY)

    map = [ [ 0 for x in range(maxX-minX+1) ] for y in range(maxY-minY+1) ]

    for x, y, c in zip(xList, yList, cList):
        # print(x, y, c)
        map[y-minY][x-minX] = c

    return map

def readTestMap():
    map = []
    for i, line in enumerate(open(file)):
        line = line.strip('\n')
        map.append([ 0 if c == ' ' else 1 for c in line ])
    return map

map = readMap()
# map = readTestMap()

def printMap():
    print('/')
    for line in map:
        print('|' + (''.join([ (' ' if c == 0 else '.' if c == '.' else '#') for c in line ])) + '|' )
    print('\\')

# printMap()

printMap()

for y, line in enumerate(map):
    inWall = None
    inside = False
    for x, c in enumerate(line):
        if c != 0:
            sum += 1
            if inWall is None:
                inWall = x
        else:
            if inWall is not None:
                # simple wall
                if inWall == x-1:
                    inside = not inside
                else:
                    nw = False if y == 0 else (map[y-1][inWall] != 0)
                    ne = False if y == 0 else (map[y-1][x-1] != 0)
                    sw = False if y == len(map)-1 else (map[y+1][inWall] != 0)
                    se = False if y == len(map)-1 else (map[y+1][x-1] != 0)
                    # print(nw, ne, sw, se)
                    if nw != ne or sw != se:
                        inside = not inside
                inWall = None
            if inside:
                map[y][x]='.'
                sum += 1

printMap()

print(sum)
