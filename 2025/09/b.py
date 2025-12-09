#!/bin/env python3
import sys

file = sys.argv[1]

tiles = []

def into(ta, tb, tc):
    return tc[0]>ta[0] and tc[0]<tb[0] and tc[1]>ta[1] and tc[1]<tb[1]



for i, line in enumerate(open(file)):
    line = list(map(int, line.strip('\n').split(',')))
    tiles.append([line[0], line[1]])

# print(tiles)

minx=1000000
maxx=0
miny=1000000
maxy=0

for x, y in tiles:
    minx = min(minx, x)
    maxx = max(maxx, x)
    miny = min(miny, y)
    maxy = max(maxy, y)

ground = [ [ '.' for x in range(minx, maxx+1) ] for y in range(miny, maxy+1) ]
print(f"{minx}..{maxx} , {miny}..{maxy}")

def draw(x0, y0, x1, y1):
    global minx, miny, maxx, maxy, ground

    # print(f" #[{x1},{y1}]")
    ground[y1-miny][x1-minx] = '#'
    if x0 == x1:
        for y in range(min(y0, y1)+1, max(y0, y1)):
            ground[y-miny][x0-minx] = 'X'
    else:
        for x in range(min(x0, x1)+1, max(x0, x1)):
            ground[y0-miny][x-minx] = 'X'

x0, y0 = tiles[0]
ground[y0-miny][x0-minx] = '#'
for x1, y1 in tiles[1:]:
    draw(x0, y0, x1, y1)
    x0, y0 = x1, y1
draw(x0, y0, tiles[0][0], tiles[0][1])

for line in ground:
    print(line)
print("\n")

for y, line in enumerate(ground):
    prev = '.'
    fill = '.'
    for x, cell in enumerate(line):
        if prev == '.' and cell != '.':
            fill = '.' if fill == 'x' else 'x'
        elif fill == 'x':
            ground[y][x] = fill
        prev = cell

for line in ground:
    print(line)

# max_area = 0

# for i, ta in enumerate(tiles):
#     for j, tb in enumerate(tiles[i+1:]):
#         print(f"check {i}:{ta} / {j}:{tb}")
#         ok = True
#         for k, tc in enumerate(tiles):
#             if k != i and k != j and into(ta, tb, tc):
#                 print(f"  fail because of {k}:{tc}")
#                 ok = False
#                 break
#         if ok:
#             max_area = max (max_area, (tb[0]-ta[0]+1) * (tb[1]-ta[1]+1))
#             print(f"  ⇒ {max_area}")
        
# print(max_area)
