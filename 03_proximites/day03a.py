#!/bin/env python3

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

prev=None
curr=None
next=None
parts = []

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
            if c == '.':
                symbols.append(False)
            else:
                symbols.append(True)
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

    if curr is not None:
        symbols = curr[1]
        for i in range(0, len(symbols)):
            if symbols[i]:
                toSet = {}
                toSet['c'] = curr[0][i]
                if prev is not None:
                    toSet['p'] = prev[0][i]
                if next is not None:
                    toSet['n'] = next[0][i]
                print(toSet)
                for ps in toSet.values():
                    for p in ps:
                        p['found'] = True

print(parts)
for part in parts:
    if part['found']:
        sum += part['value']
print(sum)
