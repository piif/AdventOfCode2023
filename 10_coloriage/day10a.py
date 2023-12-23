#!/bin/env python3

sum = 0

# file = 'sample_a.txt'
# file = 'sample_b.txt'
file = 'data_a.txt'

bricks = {
    '|': ( 'n', 's' ),
    '-': ( 'w', 'e' ),
    'L': ( 'n', 'e' ),
    'J': ( 'n', 'w' ),
    '7': ( 'w', 's' ),
    'F': ( 'e', 's' ),
    '.': ( )
}
directions = {
    'n': [  0, -1 ],
    'w': [ -1,  0 ],
    'e': [  1,  0 ],
    's': [  0,  1 ]
}

def connected(maze, size, start):
    result = []
    (szx, szy) = size
    (stx, sty) = start
    for dir, (dx, dy) in directions.items():
        (x, y) = (stx-dx , sty-dy)
        if x >= 0 and x <= szx and y >= 0 and y <= szy:
            brick = maze[y][x]
            if dir in bricks[brick]:
                result.append( (x, y) )
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
f = open(file, 'r')
for i, line in enumerate(f.readlines()):
    print("read " + line)
    maze.append(line.strip('\n'))
    try:
        s = line.index('S')
        start = ( s, i )
    except:
        pass

size = ( len(maze[0]), len(maze) )
print(maze, size, start)
prev = [ start, start ]
curr = connected(maze, size, start)
path = 1

while curr[0] != curr[1]:
    next = [ getNext(maze, prev[0], curr[0]), getNext(maze, prev[1], curr[1]) ]
    print(next)
    prev = curr
    curr = next
    path += 1

print(path)
