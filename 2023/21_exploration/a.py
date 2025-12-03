#!/bin/env python3

sum = 0

# file = 'sample_a.txt'
# STEPS = 6
file = 'data_a.txt'
STEPS = 64

map = []
start = None
for y, line in enumerate(open(file)):
    line = line.strip('\n')
    # print("read " + line)
    map.append(line)
    if 'S' in line:
        start = (line.index('S'), y)

width = len(map[0])
height = len(map)
print(width, height, start)

plots = [ start ]
for step in range(STEPS):
    newPlots = []
    for plot in plots:
        (x, y) = plot
        if x > 0 and map[y][x-1] != '#' and (x-1, y) not in newPlots:
            newPlots.append((x-1, y))
        if x+1 < width and map[y][x+1] != '#' and (x+1, y) not in newPlots:
            newPlots.append((x+1, y))
        if y > 0 and map[y-1][x] != '#' and (x, y-1) not in newPlots:
            newPlots.append((x, y-1))
        if y+1 < height and map[y+1][x] != '#' and (x, y+1) not in newPlots:
            newPlots.append((x, y+1))
    plots = newPlots

print(len(plots))
