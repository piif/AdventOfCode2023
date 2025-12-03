#!/bin/env python3

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

def check(tab, a, b):
    m = len(tab)-1
    while True:
        # print("->", a, b)
        if a==0 or b==m:
            return True
        a -= 1
        b += 1
        if tab[a] != tab[b]:
            return False

def solve(tab):
    print(tab)
    prev = tab[0]
    for i, t in enumerate(tab[1:]):
        if t == prev:
            # print("check", i, i+1)
            if check(tab, i, i+1):
                return i+1
        prev = t
    return 0

horiz = []
vert = None

for i, line in enumerate(open(file)):
    print("read " + line)

    if line == "":
        sum += solve(horiz) * 100 + solve(vert)
        horiz = []
        vert = None
        continue

    if vert is None:
        vert = [ 1 if c == '#' else 0 for c in line ]
    else:
        for i, c in enumerate(line):
            if c == '#':
                vert[i] = vert[i]*2 + 1
            else:
                vert[i] = vert[i]*2
    h = 0
    for c in line:
        h *= 2
        if c == '#':
            h += 1
    horiz.append(h)

sum += solve(horiz) * 100 + solve(vert)

print(sum)
