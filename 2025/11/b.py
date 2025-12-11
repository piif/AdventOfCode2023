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
        "found": 0,

    }

# print_graph(graph)
print()

def pathes(src, thru):
    # print(f"pathes {src} thru {thru}")
    new_thru = thru + [src]
    node = graph[src]
    # if node['found'] != 0:
    #     return node['found']

    found = 0
    for dst in node['dst']:
        if dst == 'out':
            if 'dac' in thru and 'fft' in thru:
                # print(f"found {new_thru}")
                found += 1
        else:
            found += pathes(dst, new_thru)
        
    node['found'] = found
    # print(f"{' '*len(new_thru)}pathes {src}:{node} → {found}")
    return found


total = pathes('svr', [])

print(total)
