#!/bin/env python3
import sys

total = 0

file = sys.argv[1]

def print_graph(graph):
    for src, item in graph.items():
        print(f"{src}: {item['dst']} {item['found']}")

graph = {}
for i, line in enumerate(open(file)):
    line = line.strip('\n').split(' ')
    src = line[0][0:-1]
    graph[src] = {
        "dst": line[1:],
        "found": 0
    }

# print_graph(graph)
print()

def pathes(src):
    node = graph[src]
    if node['found'] != 0:
        return node['found']

    # print(f"pathes {src}:{node}")
    found = 0
    for dst in node['dst']:
        if dst == 'out':
            found += 1
        else:
            found += pathes(dst)
        
    node['found'] = found
    return found


total = pathes('you')

print(total)
