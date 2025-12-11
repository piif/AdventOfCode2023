#!/bin/env python3
import sys

total = 0

file = sys.argv[1]

def print_graph(graph):
    for src, item in graph.items():
        print(f"{src}: {item['dst']} {item['found']} {item['marked']}")

graph = {}
for i, line in enumerate(open(file)):
    line = line.strip('\n').split(' ')
    src = line[0][0:-1]
    graph[src] = {
        "dst": line[1:],
        "found": -1,
        "marked": 0
    }

# graph['out'] = { 'dst': [], 'found': 0 }
# print_graph(graph)
print()

def pathes(src, target, excluded, indent=''):
    node = graph[src]
    if node['found'] != -1:
        # print(f"{indent}pathes {src}:{node} → ({node['found']})")
        return node['found']
    elif node['marked'] == 1:
        return 0
    # print(f"{indent}pathes {src}:{node}")

    node['marked'] = 1

    found = 0
    for dst in node['dst']:
        if dst == target:
            found += 1
        elif dst in excluded:
            node['marked'] = 0
            return 0
        else:
            found += pathes(dst, target, excluded, indent+'  ')
        
    node['found'] = found
    # print(f"{indent}pathes {src}:{node} → {found}")
    node['marked'] = 0
    return found


def reset_graph():
    for src, item in graph.items():
        item['found'] = -1


# svr_out = pathes('svr', 'out', set(['svr']))
# reset_graph()
# print(f"svr_out : {svr_out}")

svr_dac = pathes('svr', 'dac', set(['svr', 'fft', 'out']))
# print_graph(graph)
reset_graph()
print(f"svr_dac : {svr_dac}")

dac_fft = pathes('dac', 'fft', set(['svr', 'dac', 'out']))
reset_graph()
print(f"dac_fft : {dac_fft}")

fft_out = pathes('fft', 'out', set(['svr', 'dac', 'fft']))
reset_graph()
print(f"fft_out : {fft_out}")

fft_dac = pathes('fft', 'dac', set(['svr', 'fft', 'out']))
reset_graph()
print(f"fft_dac: {fft_dac}")

dac_out = pathes('dac', 'out', set(['svr', 'dac', 'fft']))
reset_graph()
print(f"dac_out: {dac_out}")

svr_fft = pathes('svr', 'fft', set(['svr', 'dac', 'out']))
reset_graph()
print(f"svr_fft: {svr_fft}")

print(svr_dac * dac_fft * fft_out + svr_fft * fft_dac * dac_out)
