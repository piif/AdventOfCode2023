#!/bin/env python3
import time

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

def arrangements(a, n, i=0):
    # print('| '*i, "ar", a, n)
    if a == 0:
        # print('  '*i, "-> a=0", '.'*n)
        return [ '.'*n ]
    if a == n:
        # print('  '*i, "-> a=n", '#'*n)
        return [ '#'*n ]
    a1 = [ ('#' + p) for p in arrangements(a-1, n-1, i+1) ]
    a2 = [ ('.' + p) for p in arrangements(a  , n-1, i+1) ]
    # print('  '*i, '->', a1, a2)
    return a1 + a2

def permut(array, indexes = None):
    # print("permut", array, indexes)
    if indexes is None:
        indexes = [ i for i in range(len(array)) ]
    elif len(indexes) == 1:
        # print("->", [ [ array[indexes[0]] ] ])
        return [ array[indexes[0]] ]

    result = []
    for i, v in enumerate(indexes):
        result += [ array[v] + ''.join(p) for p in permut(array, indexes[:i] + indexes[(i+1):]) ]
    # print("=>", result)
    return result

# print( permut("abcde") )
# print (arrangements(3, 5))

def recordMatch(records, ranges):
    prev = None
    i = 0
    count = 0
    for r in records+'.':
        if r == '#':
            count += 1
        elif count > 0:
            if ranges[i] != count:
                return False
            i += 1
            count = 0
    # if i != len(records):
    #     return False
    return True

def assemble(records, mask):
    result = ""
    i = 0
    for r in records:
        if r == '?':
            result += mask[i]
            i+=1
        else:
            result += r
    return result

f = open(file, 'r')
for line in f.readlines():
    print("read " + line)
    (records, ranges) = line.split()
    ranges= [ int(i) for i in ranges.split(',') ]

    nbSprings = 0
    for i in ranges:
        nbSprings += i
    nbKnowns = records.count('#')
    nbUnknowns = records.count('?')
    toFind = nbSprings - nbKnowns
    mask = '#'*toFind + '.'*(nbUnknowns - toFind)

    print(records, ranges, mask)
    perms = arrangements(toFind, nbUnknowns)
    print(time.localtime(), "perms", len(perms))
    for perm in perms:
        test = assemble(records, perm)
        match = recordMatch(test, ranges)
        # print(test, match)
        if match:
            sum += 1

    print(sum)
