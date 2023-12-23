#!/bin/env python3
import re

# file = 'sample_a.txt'
# file = 'sample_c.txt'
file = 'data_a.txt'

bricks = {
    '|': [ 'n', 's' ],
    '-': [ 'w', 'e' ],
    'L': [ 'n', 'e' ],
    'J': [ 'n', 'w' ],
    '7': [ 'w', 's' ],
    'F': [ 'e', 's' ],
    '.': [ ]
}
directions = {
    'n': [  0, -1 ],
    'w': [ -1,  0 ],
    'e': [  1,  0 ],
    's': [  0,  1 ]
}

opposites = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}

def connected(maze, size, start):
    result = []
    myDirs = []
    (szx, szy) = size
    (stx, sty) = start
    for dir, (dx, dy) in directions.items():
        (x, y) = (stx-dx , sty-dy)
        if x >= 0 and x <= szx and y >= 0 and y <= szy:
            brick = maze[y][x]
            if dir in bricks[brick]:
                myDirs.append(opposites[dir])
                result.append( (x, y) )
    print("start dirs", myDirs)
    for brick, dirs in bricks.items():
        if dirs == myDirs or dirs == [ myDirs[1], myDirs[0] ] :
            fill[sty][stx] = brick
    return result

def getNext(maze, prev, curr):
    (px, py) = prev
    (cx, cy) = curr
    dirs = bricks[maze[cy][cx]]
    for d in dirs:
        (dx, dy) = directions[d]
        (nx, ny) = (cx+dx , cy+dy)
        if (nx, ny) != (px, py):
            return (nx, ny)
    return None

maze = []
fill = []
f = open(file, 'r')
for i, line in enumerate(f.readlines()):
    print("read " + line)
    line = re.split('', line.strip('\n'))[1:-1]
    maze.append(line)
    fill.append([ '.' for i in range(len(line))])
    try:
        s = line.index('S')
        start = ( s, i )
    except:
        pass

size = ( len(maze[0]), len(maze) )
prev = [ start, start ]
curr = connected(maze, size, start)
fill[curr[0][1]][curr[0][0]] = maze[curr[0][1]][curr[0][0]]
fill[curr[1][1]][curr[1][0]] = maze[curr[1][1]][curr[1][0]]
path = 1
print(maze, fill, size, start)

while curr[0] != curr[1]:
    next = [ getNext(maze, prev[0], curr[0]), getNext(maze, prev[1], curr[1]) ]
    print(next)
    fill[next[0][1]][next[0][0]] = maze[next[0][1]][next[0][0]]
    fill[next[1][1]][next[1][0]] = maze[next[1][1]][next[1][0]]
    prev = curr
    curr = next
    path += 1

print(fill)
sum=0
for y, line in enumerate(fill):
    fillIn = False
    # inWall = False
    for x, brick in enumerate(line):
        # if inWall and brick in ('.', '|'):
        #     inWall = False
        #     fillIn = not fillIn
        if brick == '.':
            if fillIn:
                sum += 1
                fill[y][x] = "\x1b[32mX\x1b[m"
            else:
                fill[y][x] = ' '
        elif brick in ('L', 'J', '|'):
        # elif brick in ('F', '7', '|'):
            fillIn = not fillIn
        if brick == 'F':
            fill[y][x] = '\u256D'
        elif brick == '7':
            fill[y][x] = '\u256E'
        elif brick == 'J':
            fill[y][x] = '\u256F'
        elif brick == 'L':
            fill[y][x] = '\u2570'
        # else:
        #     inWall = True
    print(''.join(line), sum)
print(sum)
