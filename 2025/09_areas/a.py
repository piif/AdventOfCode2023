#!/bin/env python3
import sys

file = sys.argv[1]

tiles = []

for i, line in enumerate(open(file)):
    line = list(map(int, line.strip('\n').split(',')))
    tiles.append([line[0], line[1], line[0]*1000000 + line[1]])

# print(tiles)
tiles.sort(key=lambda x: x[2])

max_area = 0

for i, ta in enumerate(tiles):
    for tb in tiles[i+1:]:
        max_area = max (max_area, (tb[0]-ta[0]+1) * (tb[1]-ta[1]+1))
        
print(max_area)
