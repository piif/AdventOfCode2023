#!/bin/env python
import sys
from functools import reduce

total = 0

file = sys.argv[1]

problems=[]

for i, line in enumerate(open(file)):
    line = line.strip('\n')
    line = line.split()
    print(f"read {line}")

    if len(problems) == 0:
        problems = [ [ int(v) ] for v in line ]
    elif line[0] in ('+', '*'):
        for i, op in enumerate(line):
            if op == '+':
                total += sum(problems[i])
            else:
                total += reduce(lambda x,y:x*y, problems[i])
        break
    else:
        for i, v in enumerate(line):
            problems[i].append(int(v))

print(problems, line)

print(total)
