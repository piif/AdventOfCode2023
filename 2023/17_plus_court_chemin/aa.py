#!/bin/env python3

# file = 'sample_3.txt'
# file = 'sample_a.txt'
file = 'data_a.txt'

DIRS = '^<>v'
ANGLES = {
    '^': '<>',
    '<': 'v^',
    '>': 'v^',
    'v': '<>'
}

def move(x, y, dir):
    if dir =='^':
        return (x, y-1) if y > 0 else None
    elif dir =='v':
        return (x, y+1) if y < maxY else None
    elif dir =='<':
        return (x-1, y) if x > 0 else None
    elif dir =='>':
        return (x+1, y) if x < maxX else None

map = []
for i, line in enumerate(open(file)):
    map.append([ int(c) for c in line.strip('\n') ])

maxX=len(map[0])-1
maxY=len(map)-1
# print(map, maxX, maxY)
maxLoss = 10 * (maxX+1) * (maxY+1)

graph = {}
nodes = {}

def neighbours(x, y, dir):
    loss = 0
    (nx, ny) = (x, y)
    for i in range(10):
        newPos = move(nx, ny, dir)
        if newPos is None:
            continue
        (nx, ny) = newPos
        loss += map[ny][nx]
        if i>=3:
            for destDir in ANGLES[dir]:
                if (nx, ny, destDir) in graph:
                    graph[(x, y, dir)][(nx, ny, destDir)] = loss

# create graph with 4 node per block
for y, line in enumerate(map):
    for x, loss in enumerate(line):
        for dir in DIRS:
            nodes[(x, y, dir)] = (False, maxLoss, None)
            graph[(x, y, dir)] = {}

del graph[(0, 0, '<')]
del nodes[(0, 0, '<')]

graph[(0, 0, 'X')] = {
    (0, 0, '>') : 0,
    (0, 0, 'v') : 0
}
nodes[(0, 0, 'X')] = (False, 0, None)

# then add links with up to 3 steps neighbours
for y, line in enumerate(map):
    for x, loss in enumerate(line):
        for dir in DIRS:
            if (x, y, dir) in nodes:
                neighbours(x, y, dir)

# for y, line in enumerate(map):
#     for x, loss in enumerate(line):
#         for dir in DIRS:
#             if (x, y, dir) in graph:
#                 print(x, y, dir, graph[(x, y, dir)])


J = 3
def printNodes():
    print(' '*J + '|', end='')
    for x in range(maxX+1):
        for dir in DIRS:
            print('   '+dir + ' '*(J-1), end='')
        print('|', end='')
    print()

    for y in range(maxY+1):
        print(str(y).rjust(J) + '|', end='')
        for x in range(maxX+1):
            for dir in DIRS:
                if (x, y, dir) in nodes:
                    (v, d, src) = nodes[(x, y, dir)]
                    s = str(d).rjust(J) if d != maxLoss else (' ' + '-'*(J-2) + ' ')
                    if v:
                        print("\x1b[32m" + s + "\x1b[m", end='')
                    else:
                        print(s, end='')
                    if src is None:
                        print('   ', end='')
                    else:
                        print(f'{src[2]}{src[0]: >x}{src[1]: >x}', end='')
                else:
                    print(' '*J+'   ', end='')
            print('|', end='')
        print()

def algo():
    current = (0, 0, 'X')

    iter = 0
    while True:
        iter += 1
        print(iter, current)
        (x, y, dir) = current
        (visited, currLoss, src) = nodes[current]
        nodes[current] = (True, currLoss, src)

        for key, loss in graph[current].items():
            (visited, distance, src) = nodes[key]
            if visited:
                continue
            (nx, ny, ndir) = key
            if currLoss + loss < distance:
                nodes[key] = (visited, currLoss + loss, (x,y,dir))

        # printNodes()

        found = True
        result = maxLoss
        for dir in DIRS:
            l = nodes[(maxX, maxY, dir)][1]
            if l == maxLoss:
                found = False
                break
            if l < result:
                result = l
        if found:
            return result

        minDistance = maxLoss
        current = None
        for key, (visited, distance, src) in nodes.items():
            if not visited and distance < minDistance:
                current = key
                minDistance = distance
        if current is None:
            print("Problem ...")
            return None

result = algo()
printNodes()
print("Found", result)
