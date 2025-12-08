#!/bin/env python
import sys

total = 0

file = sys.argv[1]

with open(file) as f:
    line = next(f)
    line = line.strip('\n')
    beams = set([line.index('S')])
    print(f"L0 = {line} -> {beams}")
    for i, line in enumerate(f):
        line = line.strip('\n')
        print("read " + line)
        copy = beams.copy()
        for b in copy:
            if line[b] == '^':
                total += 1
                beams.remove(b)
                beams.add(b-1)
                beams.add(b+1)

print(total)
