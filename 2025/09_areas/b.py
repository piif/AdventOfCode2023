#!/bin/env python3
import sys

file = sys.argv[1]

tiles = []

def into(ta, tb, tc):
    return tc[0]>ta[0] and tc[0]<tb[0] and tc[1]>ta[1] and tc[1]<tb[1]

# given a rectangle r and a edge e, does e "cuts" r
def cuts(rx0, ry0, rx1, ry1, ex0, ey0, ex1, ey1):
    # bounding box
    rt = min(ry0, ry1)
    rl = min(rx0, rx1)
    rb = max(ry0, ry1)
    rr = max(rx0, rx1)

    if ex0 == ex1:
        if ex0 <= rl or ex0 >= rr:
            return False
        et = min(ey0, ey1)
        eb = max(ey0, ey1)
        return et < rb and eb > rt
    else:
        if ey0 <= rt or ey0 >= rb:
            return False
        el = min(ex0, ex1)
        er = max(ex0, ex1)
        return el < rr and er > rl

print("read file")
for i, line in enumerate(open(file)):
    line = list(map(int, line.strip('\n').split(',')))
    tiles.append([line[0], line[1]])

max_area = 0

# for each possible rectangle
for i, ta in enumerate(tiles):
    for tb in tiles[i+1:]:
        valid = True
        # for each edge
        i1 = 1
        for x0, y0 in tiles:
            x1, y1 = tiles[i1 % len(tiles)]
            if cuts(ta[0], ta[1], tb[0], tb[1], x0, y0, x1, y1):
                # print(ta, tb, "cuts", x0, y0, x1, y1)
                valid = False
                break
            i1 += 1
        if valid:
            max_area = max (max_area, (abs(tb[0]-ta[0])+1) * (abs(tb[1]-ta[1])+1))
            # print(ta, tb, max_area)

print(max_area)