#!/bin/env python3

file = 'sample_a.txt'
# file = 'data_a.txt'

map = []

def readMap():
    global map
    for y, line in enumerate(open(file)):
        line = line.strip('\n')
        print("read " + line)
        l = []
        for x, c in enumerate(line):
            l.append((c, None))
        map.append(l)

def printMap():
    for line in map:
        for (kind, dist) in line:
            if dist is not None:
                d = f'{dist:3}'
            else:
                d = f'   '
            print(f'{d}{kind}', end='')
        print()

def checkMove(x, y, nx, ny):
    if nx not in range(width) or ny not in range(height):
        return False
    (kind, distance) = map[ny][nx]
    if kind == '#':
        return False
    return distance is None

def computeDistances():
    plots = [ start ]
    step = 1
    while True:
        newPlots = []
        for plot in plots:
            (x, y) = plot
            if map[y][x] is None:
                print(f"Problem at {plot}")
                return
            (kind, distance) = map[y][x]

            if kind in '.<' and checkMove(x, y, x-1, y):
                newPlots.append((x-1, y))
                map[y][x-1] = (kind, step)
            if kind in '.>' and checkMove(x, y, x+1, y):
                newPlots.append((x+1, y))
                map[y][x+1] = (kind, step)
            if kind in '.^' and checkMove(x, y, x, y-1):
                newPlots.append((x, y-1))
                map[y-1][x] = (kind, step)
            if kind in '.v' and checkMove(x, y, x, y+1):
                newPlots.append((x, y+1))
                map[y+1][x] = (kind, step)
        if len(newPlots) == 0:
            break
        plots = newPlots
        step += 1


readMap()

width = len(map[0])
height = len(map)
start = (map[0].index(('.', None)), 0)
map[0][start[0]] = ('.', 0)
end = (map[-1].index(('.', None)), height-1)

printMap()
print(f'size {width}x{height}, from {start} to {end}')

computeDistances()
printMap()
