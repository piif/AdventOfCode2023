#!/bin/env python3

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

prev=None
curr=None
next=None
parts = []

def findGears(symbols, prev, curr, next):
    sum = 0
    for i in range(0, len(symbols)):
        if symbols[i]:
            gears = curr[i]
            if prev is not None:
                gears += prev[i]
            if next is not None:
                gears += next[i]
            print(gears)
            if len(gears) > 2:
                print('more than 2 parts !')
            elif len(gears) == 2:
                sum += gears[0]['value'] * gears[1]['value']
    return sum

def parse(line):
    num = None
    part = None
    refs = []
    symbols = []
    for c in line:
        if c >= '0' and c <= '9':
            symbols.append(False)
            if part is None:
                part = {
                    "value": int(c),
                    "found": False
                }
                parts.append(part)
                ref = len(parts)
                if len(refs) != 0:
                    refs[-1].append(part)
                refs.append([ part ])
            else:
                part['value'] = part['value']*10 + int(c)
                refs.append([ part ])
        else:
            if part is not None:
                refs.append([ part ])
                part = None
            else:
                refs.append([])
            if c == '*':
                symbols.append(True)
            else:
                symbols.append(False)
    return (refs, symbols)

f = open(file, 'r')
for line in f.readlines():
    line = line.rstrip('\n')
    print("read " + line)
    (refs, symbols) = parse(line)
    # print(refs, symbols)
    if prev is None:
        prev = (refs, symbols)
    elif curr is None:
        curr = (refs, symbols)
    elif next is None:
        next = (refs, symbols)
    else:
        prev = curr
        curr = next
        next = (refs, symbols)
    # print(prev, curr, next)

    if curr is not None and next is not None:
        sum += findGears(curr[1], prev[0], curr[0], next[0])

# print(parts)
for part in parts:
    if part['found']:
        sum += part['value']
print(sum)
