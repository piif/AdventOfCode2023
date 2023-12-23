#!/bin/env python3

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

limit = 1
def distance(a, b):
    if a == b:
        return 0
    d = 0
    for (aa, bb) in zip(a, b):
        if aa != bb:
            d += 1
            if d > limit:
                return d
    return d

# print(distance("abc", "abc")) # 0
# print(distance("abc", "aba")) # 1
# print(distance("abc", "aaa")) # 2
# print(distance("abc", "ddd")) # 2

def check(tab, a, b):
    m = len(tab)-1
    d = 0
    while True:
        d += distance(tab[a], tab[b])
        # print("->", a, b)
        if d > limit:
            return False
        if a==0 or b==m:
            return d == limit
        a -= 1
        b += 1

def solve(tab):
    # print(tab)
    prev = tab[0]
    d = 0
    for i, t in enumerate(tab[1:]):
        d = distance(prev, t)
        # print(i, prev, t, d)
        if d <= limit:
            # print("check", i, i+1)
            if check(tab, i, i+1):
                return i+1
        prev = t
    return 0

horiz = []
vert = None

for i, line in enumerate(open(file)):
    line = line.strip('\n')
    print("read " + line)
    if line == "":
        s = solve(horiz)
        if s != 0:
            sum += s * 100
        else:
            sum += solve(vert)
        print(sum)
        horiz = []
        vert = None
        continue

    if vert is None:
        vert = [ c for c in line ]
    else:
        for i, c in enumerate(line):
            vert[i] += c
    horiz.append(line)

sum += solve(horiz) * 100 + solve(vert)

print(sum)
