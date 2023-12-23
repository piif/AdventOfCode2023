#!/bin/env python3

# file = 'sample_a.txt'
file = 'data_a.txt'

def display(energy):
    for line in energy:
        print(''.join(['[' + e.ljust(4) + ']' for e in line]))

map=[ line.strip('\n') for line in open(file) ]
for line in map:
    print(line)

maxX=len(map[0])-1
maxY=len(map)-1

slash={
    'r': 't',
    'l': 'b',
    't': 'r',
    'b': 'l'
}
backslash={
    'r': 'b',
    'l': 't',
    't': 'l',
    'b': 'r'
}

def move(x, y, dir):
    if dir =='t':
        return (x, y-1, dir) if y > 0 else None
    elif dir =='b':
        return (x, y+1, dir) if y < maxY else None
    elif dir =='l':
        return (x-1, y, dir) if x > 0 else None
    elif dir =='r':
        return (x+1, y, dir) if x < maxX else None

def convert(x, y, dir):
    # print("convert", x, y, dir)

    block=map[y][x]
    other = None
    if block == '/':
        dir = slash[dir]
    elif block == '\\':
        dir = backslash[dir]
    elif block == '-':
        if dir in 'tb':
            dir = 'l'
            other = move(x, y, 'r')
    elif block == '|':
        if dir in 'lr':
            dir = 't'
            other = move(x, y, 'b')
    next = move(x, y, dir)

    result = []
    if next is not None:
        result.append(next)
    if other is not None:
        result.append(other)
    return result

def tryWith(entry):
    todo=[ entry ]
    energy = [ ['']*(maxX+1) for y in range(maxY+1) ]

    for t in todo:
        (x, y, dir) = t
        # print("todo", x, y, dir)

        while True:
            # print("curr", x, y, dir)
            if dir in energy[y][x]:
                # print("stop")
                break
            energy[y][x] += dir
            nexts = convert(x, y, dir)
            if len(nexts) == 0:
                break
            (x, y, dir) = nexts[0]
            if len(nexts) == 2:
                todo.append(nexts[1])

    # display(energy)
    sum = 0
    for line in energy:
        sum += maxX+1 - line.count('')
    return sum

m = 0
for x in range(maxX+1):
    b = tryWith((x,0,'b'))
    t = tryWith((x,maxY,'t'))
    m = max(m, b, t)

for y in range(maxY+1):
    r = tryWith((0,y,'r'))
    l = tryWith((maxX,y,'l'))
    m = max(m, r, l)

print(m)