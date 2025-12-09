#!/bin/env python3
import sys

limit = int(sys.argv[1])
file = sys.argv[2]

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

graph = []

for line in range(len(points)):
    a = points[line]
    for col in range(line+1, len(points)):
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

    if links_done == limit:
        break

circuits = sorted(list(circuits), reverse=True, key=(lambda x: len(x)))
print_circuits(circuits)

found = 0
prev = None
total = 1
for c in circuits[0:3]:
    total *= len(c)

print(total)
