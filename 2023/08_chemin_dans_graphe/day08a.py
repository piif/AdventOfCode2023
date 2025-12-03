#!/bin/env python3

import re

# file = 'sample_a.txt'
# file = 'sample_b.txt'
file = 'data_a.txt'

f = open(file, 'r')
directions = f.readline().strip('\n')
f.readline()
map = {}

for line in f.readlines():
    print("read " + line)
    m = re.match("(\S*) = \((\S*), (\S*)\)", line.strip('\n'))
    map[m[1]] = [ m[2], m[3] ]

print(map)

def navigate():
    step = 'AAA'
    steps = 0
    while True:
        for d in directions:
            next = map[step]
            print(step, d, next)
            if d == 'L':
                step = next[0]
            else:
                step = next[1]
            steps += 1
            if step == 'ZZZ':
                return steps;

steps = navigate()

print(steps)
