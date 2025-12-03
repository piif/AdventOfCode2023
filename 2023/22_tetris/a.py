#!/bin/env python3
import re

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

maxX = 0
maxY = 0
maxZ = 0

class Point:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __str__(self):
        return f"({self.x} {self.y} {self.z})"

class Cube:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        if (a.x > b.x):
            print("switch x")
            (a.x, b.x) = (b.x, a.x)
        if (a.y > b.y):
            print("switch y")
            (a.y, b.y) = (b.y, a.y)
        if (a.z > b.z):
            print("switch z")
            (a.z, b.z) = (b.z, a.z)
        if a.x != b.x:
            self.dir = 'x'
        elif a.y != b.y:
            self.dir = 'y'
        else:
            self.dir = 'z'

    def __str__(self):
        return f"[ {self.dir} {self.a} {self.b} ]"

cubes = []
for i, line in enumerate(open(file)):
    line = line.strip('\n')
    # print("read " + line)
    coords = re.match("(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)", line).groups()
    cube = Cube(Point(*coords[0:3]), Point(*coords[3:]))
    maxX = max(maxX, cube.a.x, cube.b.x)
    maxY = max(maxY, cube.a.y, cube.b.y)
    maxZ = max(maxZ, cube.a.z, cube.b.z)
    # print(cube)
    cubes.append(cube)

print(maxX, maxY, maxZ)

bottom = [ [ 0 for x in range(maxX+1) ] for y in range(maxY+1) ]
cubes.sort(key = lambda cube: cube.a.z)

space = [ [ [ None for x in range(maxX+1) ] for y in range(maxY+1) ] ]

def stack(x, y, z, i):
    while len(space) <= z:
        print("stack", z, len(space))
        space.append([ [ None for xx in range(maxX+1) ] for yy in range(maxY+1) ])
    space[z][y][x] = i

for i, cube in enumerate(cubes):
    fall = maxZ
    if cube.dir == 'x':
        for x in range(cube.a.x, cube.b.x+1):
            fall = min(fall, cube.a.z - bottom[cube.a.y][x])
    elif cube.dir == 'y':
        for y in range(cube.a.y, cube.b.y+1):
            fall = min(fall, cube.a.z - bottom[y][cube.a.x])
    else:
        fall = cube.a.z - bottom[cube.a.y][cube.a.x]

    if fall != 0:
        cube.a.z -= fall
        cube.b.z -= fall
        print(fall, '->', cube)

        if cube.dir == 'x':
            for x in range(cube.a.x, cube.b.x+1):
                bottom[cube.a.y][x] = cube.a.z+1
                stack(x, cube.a.y, cube.a.z, i)
        elif cube.dir == 'y':
            for y in range(cube.a.y, cube.b.y+1):
                bottom[y][cube.a.x] = cube.a.z+1
                stack(cube.a.x, y, cube.a.z, i)
        else:
            bottom[cube.a.y][cube.a.x] = cube.b.z + 1
            for z in range(cube.a.z, cube.b.z+1):
                stack(cube.a.x, cube.a.y, z, i)

for cube in cubes:
    print(cube)

for plane in space:
    for line in plane:
        print(line, end='')
    print()

def ontop(cube):
    result = []
    if cube.b.z == len(space)-1:
        return result

    if cube.dir == 'x':
        for x in range(cube.a.x, cube.b.x+1):
            t = space[cube.a.z+1][cube.a.y][x]
            if t is not None and t not in result:
                result.append(t)
    elif cube.dir == 'y':
        for y in range(cube.a.y, cube.b.y+1):
            t = space[cube.a.z+1][y][cube.a.x]
            if t is not None and t not in result:
                result.append(t)
    else:
        t = space[cube.b.z+1][cube.b.y][cube.b.x]
        if t is not None:
            result = [ t ]
    return result

def onlyUnder(bottom, top):
    if top.dir == 'x':
        for x in range(top.a.x, top.b.x+1):
            t = space[top.a.z-1][top.a.y][x]
            if t is not None and t != bottom:
                print("  found", t)
                return False
    elif top.dir == 'y':
        for y in range(top.a.y, top.b.y+1):
            t = space[top.a.z-1][y][top.a.x]
            if t is not None and t != bottom:
                print("  found", t)
                return False
    else:
        return True
    return True

for i, cube in enumerate(cubes):
    removable = True
    for t in ontop(cube):
        print(t, "on top of", i)
        if onlyUnder(i, cubes[t]):
            print("  ", i, "only under", t)
            removable = False
            break
    if removable:
        sum += 1
        print(i, cube)

print(sum)