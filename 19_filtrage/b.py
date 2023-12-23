#!/bin/env python3
import re

# file = 'sample_a.txt'
file = 'data_a.txt'

functions = {}

def parseCode(line):
    global functions
    (name, spec) = re.match("(.*)\{(.*)\}", line).groups()
    tests = []
    for cond in spec.split(','):
        # print("# cond = ", cond)
        if ':' in cond:
            (field, oper, value, dest) = re.match("([xmas])([<>])(\d+):(.+)", cond).groups()
            tests.append( (field, oper, int(value), dest) )
        else:
            tests.append( (None, None, None, cond) )
    functions[name] = tests

for i, line in enumerate(open(file)):
    line = line.strip('\n')
    # print("# read " + line)
    if line == "":
        break
    parseCode(line)

for k, v in functions.items():
    print(k.ljust(3), v)

def splitRange(input, oper, value):
    (min, max) = input
    if oper == '<':
        if min >= value:
            return (None, input)
        elif max < value:
            return (input, None)
        else:
            return ((min, value-1), (value, max))
    else:
        if min > value:
            return (input, None)
        elif max <= value:
            return (None, input)
        else:
            return ((value+1, max), (min, value))

def compute(functionName, input, indent = 0):
    # print(indent*'  ', functionName, input)
    if functionName == 'A':
        # print(indent*'  ', 'A')
        return [ input ]
    elif functionName == 'R':
        # print(indent*'  ', 'R')
        return []
    result = []
    for (field, oper, value, dest) in functions[functionName]:
        if oper is None:
            result += compute(dest, input, indent + 1)
            return result
        (yes, no) = splitRange(input[field], oper, value)
        # print(f'{indent*"  "} > splitRange({input[field]}, {oper}, {value}) => ({yes}, {no})')
        if yes is not None:
            result += compute(dest, input | {field: yes}, indent + 1)
        if no is None:
            return result
        input[field] = no

result = compute('in', {'x': (1,4000), 'm': (1,4000), 'a': (1,4000), 's': (1,4000) })

sum = 0
for parts in result:
    print(parts)
    product = 1
    for k, (min, max) in parts.items():
        product *= max - min +1
    sum += product
print(sum)