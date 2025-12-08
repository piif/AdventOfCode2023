#!/bin/env python
import sys

total = 0

file = sys.argv[1]

with open(file) as f:
    line = next(f)
    line = line.strip('\n')
    beams = [ 0 ] * len(line)
    beams[ line.index('S') ] = 1
    print(f"L0 = {line} -> {beams}")

    for i, line in enumerate(f):
        line = line.strip('\n')
        #print("read " + line)
        for b in range(0, len(beams)):
            if line[b] == '^':
                n = beams[b]
                beams[b-1] += n
                beams[b] = 0
                beams[b+1] += n
        #print(beams)

print(sum(beams))
