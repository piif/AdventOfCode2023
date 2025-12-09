#!/bin/env python3
import sys

sum = 0

file = sys.argv[1]

def consume():
    for i, line in enumerate(open(file)):
        line = line.strip('\n')
        yield i, line

ranges = []

def check(value):
    for bottom, top in ranges:
        if value >= bottom and value <= top:
            return True
    return False

consumer = consume()

while True:
    i, line = next(consumer)
    if line == "":
        break
    ranges.append([ int(v) for v in line.split('-') ])

print(ranges)

while True:
    try:
        i, line = next(consumer)
        line = int(line)
        print(f"ID {line}")
        if check(line):
            print(" OK")
            sum += 1
            
    except StopIteration:
        break

print(sum)
