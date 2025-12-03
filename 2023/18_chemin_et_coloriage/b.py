#!/bin/env python3
import re

sum = 0

# file = 'sample_a.txt'  # 24 in , 38 wall , 8 out
file = 'data_a.txt'

dirs="RDLU"

map = {}

def insertWall(y, x, dir):
    if y not in map:
        map[y] = { x: dir }
    else:
        map[y][x] = dir

commands = []
for i, line in enumerate(open(file)):
    line = line.strip('\n')
    # print(line)
    (steps, dir) = re.match('. \d+ \(#(.....)(.)\)', line).groups()
    commands.append((dirs[int(dir)], int(steps, 16)))
    # (dir, steps) = re.match('(.) (\d+) \(#.*', line).groups()
    # commands.append((dir, int(steps)))

x = 0
y = 0
minX = 0
maxX = 0

for (dir, steps) in commands:
    if dir == 'R':
        insertWall(y, x+1, 'R')
        h = steps
        x += steps
        if x > maxX:
            maxX = x
    elif dir == 'L':
        insertWall(y, x-1, 'R')
        h = steps
        x -= steps
        if x < minX:
            minX = x
    elif dir == 'U':
        while True:
            insertWall(y, x, '^')
            if steps == 0:
                break
            steps -= 1
            y -= 1
    elif dir == 'D':
        while True:
            insertWall(y, x, 'v')
            if steps == 0:
                break
            steps -= 1
            y += 1

J=3
sum = 0

# for y in sorted(map.keys()):
#     print(sorted(map[y].keys()))

for y in sorted(map.keys()):
    # print('|', end='')
    line = map[y]
    prevX = minX-1
    prevD = 'x'
    rWall = False
    for x in sorted(line.keys()):
        d = line[x]
        if d == 'R':
            rWall = True
            continue
        if prevD == '^' and d == 'v':
            sum += x-prevX
            # print('.'*(x-prevX-1) + '#', end='')
        elif prevD == 'v' and d == '^' and rWall:
            sum += x-prevX
            # print('='*(x-prevX-1)+'#', end='')
        elif prevD  == d:
            sum += x-prevX
            # print('X'*(x-prevX-1)+'#', end='')
        else:
            # print(' '*(x-prevX-1) + '#', end='')
            sum += 1
        prevX = x
        prevD = d
        rWall = False
    # print(' '*(maxX-x) + '|')

print(sum)
