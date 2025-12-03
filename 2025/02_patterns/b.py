#!/bin/env python3

import sys

total = 0
patterns = set(())

file = sys.argv[1] #'sample_a.txt'
#file = 'data_a.txt'

def checkPatterns(low, high, pattern_len, pattern_repeat):
    global patterns
    print(f"check {low} -> {high} for {pattern_repeat} patterns of {pattern_len} digits")
    for prefix in range( int(str(low)[0:pattern_len]), 1+int(str(high)[0:pattern_len]) ):
        pattern = int(str(prefix) * pattern_repeat)
        if pattern >= low and pattern <= high:
            print(f"found {pattern}")
            patterns.add(pattern)

def check(low, high, number_len):
    w = high-low
    print(f"check {low} -> {high}")

    for l in range(1, 1+number_len//2):
        if number_len % l == 0:
            checkPatterns(low, high, l, number_len // l)
    

with open(file) as f:
    for intv in f.read().split(','):
        print("read " + intv)
        low, high = intv.split('-')
        llow = len(low)
        lhigh = len(high)
        low = int(low)
        high = int(high)
        if llow != lhigh:
            # split in ranges with same length numbers
            bottom = low
            top = int('9' * llow)
            for l in range(llow, lhigh):
                check(bottom, top, l)
                bottom = top+1
                top = bottom * 10 - 1
            check(bottom, high, lhigh)
        else:
            check(low, high, llow)

print(f"=> {patterns}")
total = sum(patterns)
print(f"sum = {total}")
