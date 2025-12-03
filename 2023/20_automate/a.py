#!/bin/env python3
import re

# file = 'sample_a.txt'
# file = 'sample_b.txt'
file = 'data_a4.txt'

automate = {}

def printAutomate():
    for name, node in automate.items():
        print(f"{name:>12} : {node['kind']} {node['inputs']} -{node['state']}-> {node['outputs']}")

def hash():
    h = ''
    for name in sorted(automate.keys()):
        h += str(automate[name]['state'])
    return h

for i, line in enumerate(open(file)):
    line = line.strip('\n')
    print("read " + line)
    (kind, name, outputs) = re.match("([&%]?)(.*) -> (.*)", line).groups()
    if name == 'broadcaster':
        kind = '*'

    automate[name] = {
        'kind': kind,
        'outputs': outputs.split(', '),
        'state': 0,
        'inputs': {}
    }

for name in list(automate.keys()):
    node = automate[name]
    for out in node['outputs']:
        if out not in automate:
            print("add", out)
            automate[out] = {
                'kind': '.',
                'outputs': [],
                'state': 0,
                'inputs': { name: 0 }
            }
        else:
            automate[out]['inputs'][name] = 0

printAutomate()

def pulse(source, dest, input):
    global low, high
    if input == 1:
        high += 1
    else:
        low += 1

    # print(f"> pulse {source} -{input}-> {dest}")

    node = automate[dest]
    if node['kind'] == '.':
        state = input
    elif node['kind'] == '%':
        if input == 0:
            node['state'] = 1 - node['state']
            for o in node['outputs']:
                todo.append( (dest, o, node['state']) )
    elif node['kind'] == '&':
        node['inputs'][source] = input
        inputs = node['inputs'].values()
        st = 0
        for v in node['inputs'].values():
            if v == 0:
                st = 1
                break
        node['state'] = st
        for o in node['outputs']:
            todo.append( (dest, o, node['state']) )
    elif node['kind'] == '*':
        node['state'] = input
        for o in node['outputs']:
            todo.append( (dest, o, node['state']) )
    # printAutomate()

cache = {}
lows = []
highs = []

MAX = 1000000
loop = None
for iter in range(MAX):
    (low, high) = (0, 0)
    todo = [ (None, 'broadcaster', 0) ]
    while len(todo) > 0:
        # print("todo", todo)
        (source, dest, state) = todo[0]
        del todo[0]
        pulse(source, dest, state)

    lows.append(low)
    highs.append(high)

    h = hash()
    if h in cache:
        loop = cache[h]
        print("loop", iter, loop)
        break

    cache[h] = iter
    # printAutomate()

# print(lows)
# print(highs)

if loop is None:
    print(sum(lows) * sum(highs))
else:
    w = iter-loop
    t = MAX-loop
    low = sum(lows[loop:iter])
    low *= t // w
    low += sum(lows[:loop]) + sum(lows[loop:(loop + t % w)])

    high = sum(highs[loop:iter])
    high *= t // w
    high += sum(highs[:loop]) + sum(highs[loop:(loop + t % w)])

    print(low, high, low*high)