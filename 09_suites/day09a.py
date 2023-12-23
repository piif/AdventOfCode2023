#!/bin/env python3

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

def extrapolate(list):
    stack = [ list ]
    while True:
        stop = True
        next = []
        a = list[0]
        for b in list[1:]:
            s = b-a
            if s != 0:
                stop = False
            next.append(s)
            a = b
        if stop:
            break
        stack.insert(0, next)
        list = next
    print(stack)
    next = 0
    for list in stack:
        next += list[-1]
    return next

f = open(file, 'r')
for line in f.readlines():
    print("read " + line)
    list = [ int(i) for i in line.split() ]
    sum += extrapolate(list)

print(sum)
