#!/bin/env python3

import re

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

max={
    'red'  : 12,
    'green': 13,
    'blue' : 14
}

# def parseGame(line):
#     m = re.match("Game (\d+): (.*)", line)
#     game={
#         'game': m[1],
#         'sets': []
#     }
#     sets=m[2].split('; ');
#     for set in sets:
#         m=re.findall("(\d+) (\w+)", set)
#         cubes={}
#         for match in m:
#             cubes[match[1]] = match[0]
#         game['sets'].append(cubes)
#     print(game)

def parseGame(line):
    m = re.match("Game (\d+): (.*)", line)
    game= int(m[1])
    sets=m[2].split('; ');
    for set in sets:
        m=re.findall("(\d+) (\w+)", set)
        for (num, color) in m:
            num = int(num)
            if color not in max:
                print(f'unexpected {color} color')
                return 0
            if num > max[color]:
                return 0
    return game

f = open(file, 'r')
for line in f.readlines():
    print("read " + line)
    sum += parseGame(line)

print(sum)
