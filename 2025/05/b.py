#!/bin/env python3
import sys

sum = 0

file = sys.argv[1]

ranges = []

def add_to_ranges(bottom, top):
    global ranges
    new_ranges = []
    for b, t in ranges:
        if b > top or t < bottom:
            new_ranges.append([b, t])
            continue
        if b < bottom:
            bottom = b
        if t > top:
            top = t
    new_ranges.append([bottom, top])
    ranges = new_ranges

for i, line in enumerate(open(file)):
    line = line.strip('\n')
    if line == "":
        break
    print("read " + line)
    add_to_ranges(*[ int(v) for v in line.split('-') ])
    # print(ranges)

print(ranges)

for b, t in ranges:
    sum += t - b + 1

print(sum)