#!/bin/env python3
import re

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

def hash(s):
    h = 0
    for c in s:
        h = ( (h + ord(c) ) * 17 ) % 256
    return h

boxes = [ [] for i in range(256) ]

def power():
    sum = 0
    for b, box in enumerate(boxes):
        for s, slot in enumerate(box):
            sum += (b+1) * (s+1) * int(slot[1])
    return sum

input = open(file).read().strip('\n').split(',')
for s in input:
    m = re.match("(.*)([-=])(\d*)", s)
    label=m[1]
    oper=m[2]
    value=m[3]
    h = hash(label)
    box = boxes[h]
    # print(label, oper, value, box, h)

    if oper == '-':
        for i, (l, f) in enumerate(box):
            if l == label:
                box.remove((l, f))
    elif oper == '=':
        found = False
        for i, (l, f) in enumerate(box):
            if l == label:
                box[i] = (label, value)
                found = True
                break
        if not found:
            box.append((label, value))
    # print("=>", box)

print(power())