#!/bin/env python3

import sys

sum = 0

file = sys.argv[1] #'sample_a.txt'
#file = 'data_a.txt'

def checkPatterns(low, high, pattern_len):
    global sum
    print(f"check {low} -> {high} for patterns of {pattern_len} digits")
    for prefix in range( int(str(low)[0:pattern_len]), 1+int(str(high)[0:pattern_len]) ):
        pattern = int(str(prefix) * 2)
        if pattern >= low and pattern <= high:
            print(f"found {pattern}")
            sum += pattern

def check(low, high, number_len):
    w = high-low
    # print(f"check {low} -> {high}")

    if number_len % 2 == 0:
        checkPatterns(low, high, number_len // 2)
    

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


print(f"sum = {sum}")
