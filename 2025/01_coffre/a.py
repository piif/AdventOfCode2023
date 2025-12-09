#!/bin/env python3
import sys

sum = 0

file = sys.argv[1]

pos = 50

for i, line in enumerate(open(file)):
    line = line.strip('\n')
    if line == '':
        continue

    print("read " + line)
    dir = line[0]
    move = int(line[1:])
    if dir == 'L':
        pos = (pos - move) % 100
    elif dir == 'R':
        pos = (pos + move) % 100
    else:
        raise Exception(f"Unexpected dir {dir}")

    if pos == 0:
        sum += 1

print(sum)
