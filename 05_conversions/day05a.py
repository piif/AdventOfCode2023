#!/bin/env python3

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

f = open(file, 'r')
line1 = f.readline()
(dummy, seedsStr) = line1.split(': ')
seeds = [ int(s) for s in seedsStr.split() ]
# seeds = [ { 'source': s, 'destination': None } for s in seedsStr.split() ]
print(seeds)

dummy = f.readline()

def convert(map):
    global seeds
    # print(map)
    for (i, seed) in enumerate(seeds):
        for m in map:
            if seed in range(m['from'], m['to']):
                # print(seeds[i], '+=', m['delta'])
                seeds[i] += m['delta']
                break

map = []
for line in f.readlines():
    line = line.strip('\n')
    # print("read " + line)
    if line.endswith(':'):
        if len(map) != 0:
            convert(map)
            print(seeds)
            map = []
    elif line != "":   
        (dst, src, ln) = line.split()
        map.append({ 'from': int(src), 'to': int(src)+int(ln), 'delta': int(dst)-int(src) })
convert(map)
print(seeds)
print(min(seeds))
