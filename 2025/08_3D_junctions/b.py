#!/bin/env python3
import sys

file = sys.argv[1]

def print_circuits(circuits):
    for c in circuits:
        if (len(c) > 1):
            print(c)

points = []

for i, line in enumerate(open(file)):
    line = line.strip('\n')
    point = [ int(i) for i in line.split(',')]
    # print(f"{i: 2}: {point}")
    points.append(point)

card = len(points)
graph = []

for line in range(card):
    a = points[line]
    for col in range(line+1, card):
        b = points[col]
        graph.append([line, col, (a[0]-b[0]) ** 2 + (a[1]-b[1]) ** 2 + (a[2]-b[2]) ** 2])

graph.sort(key = (lambda x: x[2]))
circuits = set()

links_done = 0
for src, dst, distance in graph:
    print(f"checking {src}={points[src]} {dst}={points[dst]} / {distance}")
    links_done += 1
    new_c = frozenset([src, dst])
    to_remove = set()
    found = 0
    for c in circuits:
        if src in c and dst in c:
            print(f"skipped")
            new_c = None
            break
        if src in c or dst in c:
            to_remove.add(c)
            new_c = new_c.union(c)
            found += 1
            if found == 2:
                break
    for c in to_remove:
        circuits.remove(c)
    if new_c is not None:
        circuits.add(new_c)
        if len(new_c) == card:
            break

print(points[src][0] * points[dst][0])
