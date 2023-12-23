#!/bin/env python3

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

f = open(file, 'r')
line1 = f.readline()
(dummy, seedsStr) = line1.split(': ')
seedranges = [ int(s) for s in seedsStr.split() ]
seeds = []
for i in range(0, len(seedranges), 2):
    seeds.append([ seedranges[i], seedranges[i]+seedranges[i+1] ])
print(seeds)

dummy = f.readline()

def convert(map, seeds):
    result = []
    # print(map)
    for (sfrom, sto) in seeds:
        found = False
        for (mfrom, mto, delta) in map:
            if sfrom >= mto or sto <= mfrom:
                continue
            if (sfrom >= mfrom):
                if sto <= mto:
                    result.append([sfrom+delta, sto+delta])
                    found = True
                    break
                else:
                    result.append([sfrom+delta, mto+delta])
                    sfrom = mto
            elif sto > mto:
                result.append([mfrom+delta, mto+delta])
                sto = mfrom
                seeds.append([mto, sto])
            else:
                result.append([mfrom+delta, sto+delta])
                sto = mfrom
                # print("else", sfrom, sto, mfrom, mto, "->", sfrom+delta, mfrom+delta, "+", sto, mfrom)
        if not found:
            result.append([sfrom, sto])
    return result

map = []
for line in f.readlines():
    line = line.strip('\n')
    # print("read " + line)
    if line.endswith(':'):
        if len(map) != 0:
            seeds = convert(map, seeds)
            print(seeds)
            map = []
    elif line != "":   
        (dst, src, ln) = line.split()
        map.append([ int(src), int(src)+int(ln), int(dst)-int(src) ])
seeds = convert(map, seeds)
print(seeds)
lowers = [ s[0] for s in seeds ]
print(min(lowers))
