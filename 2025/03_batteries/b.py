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

    jolt = 0
    imax = -1
    for j in range(0,12):
        max = 0
        for i in range(imax+1, len(bank)-11+j):
            if (bank[i]>max):
                max = bank[i]
                imax = i
        print(f"  found {max} at {imax}")
        jolt = jolt*10 + max
    print(f"  jolt = {jolt}")
    sum += jolt

print(sum)
