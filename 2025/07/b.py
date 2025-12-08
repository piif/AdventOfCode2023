#!/bin/env python
import sys

file = sys.argv[1]
lines = []

for i, line in enumerate(open(file)):
    lines.append(line.strip('\n'))
#print(lines)

def find_pathes(lines, beam, i):
    #print(f"find {beam} in {i}:{lines[0]}")
    if len(lines) == 1:
        return 1
    if lines[0][beam] == '^':
        return find_pathes(lines[1:], beam-1, i+1) + find_pathes(lines[1:], beam+1, i+1)
    else:
        return find_pathes(lines[1:], beam, i+1)

beam = lines[0].index('S')
total = find_pathes(lines[1:], beam, 1)

print(total)
