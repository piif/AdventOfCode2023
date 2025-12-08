#!/bin/env python
import sys

total = 0

file = sys.argv[1]

with open(file) as f:
    line = next(f)
    line = line.strip('\n')
    beams = [line.index('S')]
    print(f"L0 = {line} -> {beams}")
    for i, line in enumerate(f):
        line = line.strip('\n')
        #print("read " + line)
        new_beams = []
        for b in beams:
            if line[b] == '^':
                new_beams.append(b-1)
                new_beams.append(b+1)
            else:
                new_beams.append(b)
        beams = new_beams
        print(beams)

print(len(beams))
