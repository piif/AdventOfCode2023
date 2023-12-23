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

def navigate(step, directions, map):
    steps = 0
    while True:
        for d in directions:
            next = map[step]
            # print(step, d, next)
            if d == 'L':
                step = next[0]
            else:
                step = next[1]
            steps += 1
            if step[-1] == 'Z':
                return steps;

def ppcm(a,b):
    return a*b/pgcd(a,b)

def pgcd(a,b):
    while True:
        if a > b:
            r = a % b
        else:
            r = b % a
        if r == 0:
            return b
        a = b
        b = r

nbSteps = []
for step in steps:
    nbSteps.append(navigate(step, directions, map))

print(nbSteps)
result = nbSteps.pop()
for n in nbSteps:
    result = ppcm(result, n)
    print(result)