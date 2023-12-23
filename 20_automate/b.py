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
    global todo
    # print(f"> pulse {source} -{input}-> {dest}")

    if dest == 'rx' and input == 0:
        return True

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
    return False

def iterate():
    global todo
    iter = 0
    while True:
        iter += 1
        if iter % 10000 == 0:
            print(iter)
        todo = [ (None, 'broadcaster', 0) ]
        while len(todo) > 0:
            # print("todo", todo)
            (source, dest, state) = todo[0]
            del todo[0]
            if pulse(source, dest, state):
                print("Found at", iter)
                return

def findIslands():
    toKeep = [ 'rx' ]
    other = list(automate.keys())
    other.remove('rx')
    toCheck = [ 'rx' ]

    for n in toCheck:
        for p in automate[n]['inputs'].keys():
            if p not in toKeep:
                toKeep.append(p)
                other.remove(p)
                toCheck.append(p)
    print(toKeep, other)

# iterate()

def ppcm(a,b):
    return a*b/pgcd(a,b)

def pgcd(a,b):
    while True:
        if a > b:
            r = a % b
        else:
            r = b % a
        if r == 0:
            return b
        a = b
        b = r

ab = ppcm(3907, 3797)
cd = ppcm(4093, 4021)
print(ab, cd, ppcm(ab, cd))