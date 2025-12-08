#!/bin/env python
import sys
from functools import reduce

total = 0

file = sys.argv[1]

lines=[]

maxlen = 0

for i, line in enumerate(open(file)):
    lines.append(line.strip('\n'))
    maxlen = max(maxlen, len(line))
    print(f"read {line}")

print(f"maxlen={maxlen}")
values = []

for col in range(maxlen-1, -1, -1):
    value = ''.join([ line[col] if len(line)>col else '' for line in lines ]).strip()
    if value == '':
        continue
    print(f"value = '{value}'")
    if value[-1] in ('+', '*'):
        op = value[-1]
        value = int(value[0:-1])
        values.append(value)
        if op == '+':
            total += sum(values)
        else:
            total += reduce(lambda x,y:x*y, values)
        values = []
    else:
        values.append(int(value))

print(total)
