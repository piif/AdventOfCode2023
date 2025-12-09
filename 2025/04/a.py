#!/bin/env python3
import sys

sum = 0

file = sys.argv[1]

Lm1 = []
L0 = []
Lp1 = []

def check():
    global sum

    for i, x in enumerate(L0):
        if L0[i] != '@':
            continue
        neighbors = 0
        if len(Lm1) != 0:
            if i > 0 and Lm1[i-1] == '@':
                neighbors += 1
            if i < width-1 and Lm1[i+1] == '@':
                neighbors += 1
            if Lm1[i] == '@':
                neighbors += 1
        if len(Lp1) != 0:
            if i > 0 and Lp1[i-1] == '@':
                neighbors += 1
            if i < width-1 and Lp1[i+1] == '@':
                neighbors += 1
            if Lp1[i] == '@':
                neighbors += 1
        if i > 0 and L0[i-1] == '@':
            neighbors += 1
        if i < width-1 and L0[i+1] == '@':
            neighbors += 1
        if neighbors < 4:
            print(f"[{l}, {i}]")
            sum += 1


for l, line in enumerate(open(file)):
    line = line.strip('\n')
    Lm1, L0, Lp1 = L0, Lp1, [ i for i in line ]
    print(f"{l}:\n {Lm1}\n {L0}\n {Lp1}")

    if len(L0) == 0:
        continue
    width = len(L0)
    check()

Lm1, L0, Lp1 = L0, Lp1, []
check()

print(sum)
