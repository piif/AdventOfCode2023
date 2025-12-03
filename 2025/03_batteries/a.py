#!/bin/env python3
import sys

sum = 0

file = sys.argv[1]

for i, line in enumerate(open(file)):
    line = line.strip('\n')
    print("read " + line)
    if line == '':
        continue
    bank = [ int(b) for b in line ]

    max = 0
    imax = -1
    for i in range(0, len(bank)-1):
        if (bank[i]>max):
            max = bank[i]
            imax = i
    print(f"  found {max} at {imax}")
    sum += max*10

    max = 0
    for i in range(imax+1, len(bank)):
        if (bank[i]>max):
            max = bank[i]
            imax = i
    print(f"  found {max} at {imax}")
    sum += max

print(sum)
