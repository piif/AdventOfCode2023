#!/bin/env python3

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

next = None
rocks = []
for y, line in enumerate(open(file)):
    line = line.strip('\n')
    print("read " + line)

    if next is None:
        next = [ 0 ] * len(line)
        rocks = [ [] for i in range(len(line)) ]

    for x, c in enumerate(line):
        if c == '#':
            next[x] = y+1
        elif c == 'O':
            rocks[x].append(next[x])
            next[x] += 1
    # print(next, rocks)

print(y)
# print(rocks)

for col in rocks:
    for r in col:
        sum += y + 1 - r
print(sum)
