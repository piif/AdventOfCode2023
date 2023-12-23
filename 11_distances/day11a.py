#!/bin/env python3


# file = 'sample_a.txt'
file = 'data_a.txt'

f = open(file, 'r')
y = 0
scale = 1000000
galaxies = []
emptyColumns = None
for line in f.readlines():
    # print("read " + line)
    line = line .strip('\n')
    lineEmpty = True
    if emptyColumns is None:
        emptyColumns = [ True for i in range(len(line)) ]
    for x, c in enumerate(line):
        if c == '#':
            lineEmpty = False
            emptyColumns[x] = False
            galaxies.append([x, y])
    if lineEmpty:
        y += scale
    else:
        y += 1

# print(galaxies, emptyColumns)
for x in range(len(emptyColumns)-1, -1, -1):
    if emptyColumns[x]:
        for g in galaxies:
            if g[0] > x:
                g[0] += scale-1
print(galaxies)

sum = 0
for i, (x1, y1) in enumerate(galaxies):
    for (x2, y2) in galaxies[i+1:]:
        d = abs(x2-x1) + abs(y2-y1)
        # print(x1, y1, x2, y2, d)
        sum += d
print(sum)
