#!/bin/env python3
import sys

sum = 0

file = sys.argv[1]

lines = []
width=0

neighbor_positions = [
    [ -1, -1 ], [ -1, 0 ], [ -1, 1 ],
    [  0, -1 ],            [  0, 1 ],
    [  1, -1 ], [  1, 0 ], [  1, 1 ]
]

def get_position(y, x):
    if y<0 or y>=height or x<0 or x>=width:
        return ' '
    return lines[y][x]

def check(l):
    global sum

    accessibles = []

    for i, x in enumerate(lines[l]):
        if x != '@':
            continue
        neighbors = 0
        for dy, dx in neighbor_positions:
            if get_position(l+dy, i+dx) == '@':
                neighbors += 1
        if neighbors < 4:
            accessibles.append([l, i])
            # print(f"[{l}, {i}]")
            sum += 1

    return accessibles


for l, line in enumerate(open(file)):
    line = line.strip('\n')
    if line == "":
        continue
    lines.append([ i for i in line ])

# for line in lines:
#     print(line)

height = len(lines)
width = len(lines[0])

while True:
    to_remove = []

    for l in range(0, len(lines)):
        to_remove.extend(check(l))

    if len(to_remove) == 0:
        break

    for y, x in to_remove:
        # print(y, x)
        lines[y][x] = 'x'

    # for line in lines:
    #     print(line)

print(sum)
