#!/bin/env python3
import sys

total = 0

file = sys.argv[1]

def conv1(input):
    value_len = len(input)
    value = 0
    for c in input:
        value <<= 1
        if c == '#':
            value += 1
    return value, value_len


def conv2(input, ref_len):
    # print(f"conv2 {input} on {ref_len}")
    value = 0
    for b in input:
        value += 1 << (ref_len-b-1)
    return value


def solve_for_len(source, target, buttons, test_len):
    # print(f"solve_for_len({source}, {target}, {buttons}, {test_len})")
    for i, b in enumerate(buttons):
        value = source ^ b
        if test_len == 1:
            if value == target:
                return True
        else:
            if solve_for_len(value, target, buttons[i+1:], test_len-1):
                return True


def solve(target, buttons):
    max_len = len(buttons)
    test_len = 1
    while test_len < max_len:
        if solve_for_len(0, target, buttons, test_len):
            return test_len
        test_len += 1
    return None


for i, line in enumerate(open(file)):
    line = line.strip('\n').split(' ')
    target, target_len = conv1(line[0][1:-1])
    buttons = [ conv2(list(map(int, l[1:-1].split(','))), target_len) for l in line[1:-1] ]
    joltage = line[-1]
    print(f"read {target}/{target_len} , {buttons} , {joltage}")
    found = solve(target, buttons)
    print(found)
    total += found

print(total)
