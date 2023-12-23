#!/bin/env python3

# file = 'sample_a.txt'
file = 'data_a.txt'

map = []
start = None
nbPlots = 0
for y, line in enumerate(open(file)):
    line = line.strip('\n')
    # print("read " + line)
    l = []
    for x, c in enumerate(line):
        if c == 'S':
            start = (x, y)
            l.append(0)
        elif c == '.':
            l.append(-1)
            nbPlots += 1
        else:
            l.append(None)
    map.append(l)

def printMap():
    y = -start[1]
    for line in map:
        x = -start[0]
        for plot in line:
            if plot is None:
                s = '  #'
            elif plot == -1:
                s = '  .'
            else:
                s = f'{plot:3}'
            if abs(y) > start[0] - abs(x):
                print(s, end='')
            else:
                print(f'\x1b[32m{s}\x1b[m', end='')
            x += 1
        print()
        y += 1

# printMap()

width = len(map[0])
height = len(map)
print(width, height, nbPlots, start)

# compute distances into base square
plots = [ start ]
step = 1
while True:
    newPlots = []
    for plot in plots:
        (x, y) = plot
        if x > 0 and map[y][x-1] == -1 and (x-1, y) not in newPlots:
            newPlots.append((x-1, y))
            map[y][x-1] = step
        if x+1 < width and map[y][x+1] == -1 and (x+1, y) not in newPlots:
            newPlots.append((x+1, y))
            map[y][x+1] = step
        if y > 0 and map[y-1][x] == -1 and (x, y-1) not in newPlots:
            newPlots.append((x, y-1))
            map[y-1][x] = step
        if y+1 < height and map[y+1][x] == -1 and (x, y+1) not in newPlots:
            newPlots.append((x, y+1))
            map[y+1][x] = step
    if len(newPlots) == 0:
        break
    plots = newPlots
    step += 1

# printMap()

oddPlotsIn = 0
oddPlotsOut = 0
evenPlotsIn = 0
evenPlotsOut = 0

y = -start[1]
for line in map:
    x = -start[0]
    for plot in line:
        if plot is not None and plot != -1:
            if abs(y) > start[0] - abs(x):
                if plot % 2 == 0:
                    evenPlotsOut += 1
                else:
                    oddPlotsOut += 1
            else:
                if plot % 2 == 0:
                    evenPlotsIn += 1
                else:
                    oddPlotsIn += 1
        x += 1
    y += 1

print(evenPlotsIn, oddPlotsIn, evenPlotsOut, oddPlotsOut)
N = 26501365 // width
print("N=", N)
print ( pow(N+1, 2) * (oddPlotsIn + oddPlotsOut) +  pow(N, 2) * (evenPlotsIn + evenPlotsOut) - (N+1) * oddPlotsOut + N * evenPlotsOut )

# # iter 131 , 14641 plots and 13 empty
# # iter 65 , 3600 plots and 7611 empty
# # 26501365 = 131 * 202300 + 65
# # https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21

# # printMap()
# print("=>", step, len(plots))
# empty = 0
# for y, line in enumerate(map):
#     for x, plot in enumerate(line):
#         if plot == []:
#             empty += 1
# print(empty, "empty plots")