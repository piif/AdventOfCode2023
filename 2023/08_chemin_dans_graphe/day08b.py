#!/bin/env python3

import re

# file = 'sample_a.txt'
# file = 'sample_b.txt'
file = 'data_a.txt'

f = open(file, 'r')
directions = f.readline().strip('\n')
f.readline()
map = {}
steps = []

for line in f.readlines():
    # print("read " + line)
    m = re.match("(\S*) = \((\S*), (\S*)\)", line.strip('\n'))
    map[m[1]] = [ m[2], m[3] ]
    if m[1][-1] == 'A':
        steps.append(m[1])

# print(steps, map)
print(steps)

def navigate(steps, directions, map):
    nbSteps = 0
    while True:
        for d in directions:
            found = True
            nexts = []
            for step in steps:
                m = map[step]
                # print(step, d, m)
                if d == 'L':
                    next = m[0]
                else:
                    next = m[1]
                if next[-1] != 'Z':
                    found = False
                nexts.append(next)
            nbSteps += 1
            steps = nexts
            # print(steps)
            if found:
                return nbSteps;

nbSteps = navigate(steps, directions, map)

print(nbSteps)
