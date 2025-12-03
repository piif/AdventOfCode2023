#!/bin/env python3

file = 'sample_b.txt'
# file = 'data_a.txt'

def move(x, y, dir):
    if dir =='^':
        return (x, y-1) if y > 0 else None
    elif dir =='v':
        return (x, y+1) if y < maxY else None
    elif dir =='<':
        return (x-1, y) if x > 0 else None
    elif dir =='>':
        return (x+1, y) if x < maxX else None

def backmove(x, y, dir):
    if dir =='v':
        return (x, y-1) if y > 0 else None
    elif dir =='^':
        return (x, y+1) if y < maxY else None
    elif dir =='>':
        return (x-1, y) if x > 0 else None
    elif dir =='<':
        return (x+1, y) if x < maxX else None

changes = {
    '^': '^><',
    'v': 'v><',
    '<': '<v^',
    '>': '>v^'
}
cache = {}

map = []
for i, line in enumerate(open(file)):
    map.append([ int(c) for c in line.strip('\n') ])

maxX=len(map[0])-1
maxY=len(map)-1
print(map, maxX, maxY)

def printPath(path, loss):
    pathmap = [ [ ' ' ] * (maxX+1) for y in range(maxY+1) ]
    for (x, y), val in path.items():
        pathmap[y][x] = val[0]
    print('/' + '-'*(maxX+1) + '\\')
    for line in pathmap:
        print('|' + ''.join(line) + '|')
    print('\\' + '-'*(maxX+1) + '/')
    print("=>", loss)

maxLoss = 10 * (maxX+1) * (maxY+1)

def tryPath(x, y, dir, count, currloss, currpath, indent = 0):
    print('| '*indent + "tryPath", x, y, dir, count)
    key=(x, y, dir, count)
    if key in cache:
        printPath(currpath | cache[key][1], currloss + cache[key][0])

        print('| '*indent + "  cached ", cache[key])
        return cache[key][0]

    heatloss = map[y][x]
    if (x, y) == (0, 0):
        printPath(currpath, currloss + heatloss)
        cache[key] = (currloss + heatloss, currpath)
        print('| '*indent + "  =>", currloss + heatloss)
        return currloss + heatloss

    result = maxLoss
    for change in changes[dir] if count < 3 else changes[dir][1:]:
        prev = backmove(x, y, change)
        print('| '*indent + "  prev", x, y, change, prev)
        if prev is not None and prev not in currpath:
            (nx, ny) = prev
            pathLoss = tryPath(nx, ny, change, count+1 if change == dir else 1, currloss + heatloss, currpath | { prev: change+str(count) }, indent+1)
            if heatloss + pathLoss < result:
                result = heatloss + pathLoss
    print('| '*indent + "  set cache", key, "=", result)
    cache[key] = (result, currpath)
    return result

count = 0
print("***", tryPath(maxX, maxY, '>', 1, 0, { (maxX, maxY): ">1" }))
print("***", tryPath(maxX, maxY, 'v', 1, 0, { (maxX, maxY): "v1" }))
