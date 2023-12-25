#!/bin/env python3

sum = 0

file = 'sample_a.txt'
# file = 'data_a.txt'

graph = {}
def stack(src, dst):
    if src in graph:
        graph[src][dst] = ( 0, 0 ) # distance, count
    else:
        graph[src] = { dst : ( 0, 0 ) }

for i, line in enumerate(open(file)):
    line = line.strip('\n')
    # print("read " + line)
    src, arcs = line.split(': ')
    for arc in arcs.split(' '):
        stack(src, arc)
        stack(arc, src)

print(len(graph), "nodes")
maxA=0
for n, arcs in graph.items():
    maxA = max(maxA, len(arcs))
    sum+=len(arcs)
print(sum//2, "arcs", maxA, "max")

