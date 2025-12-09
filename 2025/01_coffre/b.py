#!/bin/env python3
import sys

total = 0

file = sys.argv[1]

pos = 50

for i, line in enumerate(open(file)):
    line = line.strip('\n')
    if line == '':
        continue

    
    dir = line[0]
    move = int(line[1:])
    if dir == 'L':
        newpos = pos - move
    elif dir == 'R':
        newpos = pos + move
    else:
        raise Exception(f"Unexpected dir {dir}")
    total += abs(newpos) // 100
    if newpos <= 0 and pos != 0:
        total += 1
    pos = newpos % 100
    print(f"{i: 5}:{line:<5} → {newpos: 5} → {pos: 3} ⇒ {total}")

print(total)
