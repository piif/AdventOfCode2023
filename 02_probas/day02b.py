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

def parseGame(line):
    m = re.match("Game (\d+): (.*)", line)
    game= int(m[1])
    sets=m[2].split('; ');
    gameMax={
        'red'  : 0,
        'green': 0,
        'blue' : 0
    }
    for set in sets:
        m=re.findall("(\d+) (\w+)", set)
        for (num, color) in m:
            num = int(num)
            if color not in gameMax:
                print(f'unexpected {color} color')
                return 0
            if num > gameMax[color]:
                gameMax[color] = num
    return gameMax['red'] *gameMax['green'] * gameMax['blue'] 

f = open(file, 'r')
for line in f.readlines():
    print("read " + line)
    sum += parseGame(line)

print(sum)
