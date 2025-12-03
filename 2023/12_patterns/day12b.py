#!/bin/env python3
import time

sum = 0

# file = 'sample_a.txt'
# file = 'data_b.txt'
file = 'data_a.txt'

def recordMatch(record, ranges, toFind, prev = '.'):
    # print(record, ranges, toFind, prev)
    sum = 0
    # plus rien à trouver
    if toFind == 0:
        # s'il ne reste que des . et des ? , une seule solution restante = "que des ."
        if len(record) == 0 or record.count('.') + record.count('?') == len(record):
            # print("toFind 0 -> 1")
            return 1

    # sinon (s'il en reste à trouver)
    # input vide ou que des '.' => matche pas
    if len(record) == 0 or record.count('.') == len(record):
        # print("record vide -> 0")
        return 0

        # if (len(ranges) > 1) or (len(ranges) == 1 and ranges[0] != 0) or toFind != 0:
        #     return 0
    
    rc = record[0]
    rg = ranges[0] if len(ranges) > 0 else None

    if rc == '?':
        # essayer avec un '.'
        if rg == 0:
            # print("#?.")
            sum += recordMatch(record[1:], ranges[1:], toFind, '.')
            # print("=>", sum)
        if prev == '.':
            # print(".?.")
            sum += recordMatch(record[1:], ranges, toFind, '.')
            # print("=>", sum)
        # essayer avec un '#'
        if rg is not None and rg > 0:
            # print("?#")
            sum += recordMatch(record[1:], [ rg-1 ] + ranges[1:], toFind-1, '#')
            # print("=>", sum)
        return sum

    if rc == '.':
        if rg == 0:
            # print('#.')
            return recordMatch(record[1:], ranges[1:], toFind, '.')
        if prev == '.':
            # print('..')
            return recordMatch(record[1:], ranges, toFind, '.')
    if rc == '#':
        if rg is not None and rg > 0:
            # print('#')
            return recordMatch(record[1:], [ rg-1 ] + ranges[1:], toFind, '#')

    # print('else')
    return 0

# print(recordMatch('##..##...#.', [2, 2, 1], 0))
# print(recordMatch('???..###.', [1, 1, 3], 2))
# print(recordMatch('.??..??...?##.', [1,1,3], 3))

sum = 0

f = open(file, 'r')
for line in f.readlines():
    print("read " + line)
    (records, ranges) = line.split()
    records = '?'.join([ records, records, records, records, records ])
    ranges = ','.join([ ranges, ranges, ranges, ranges, ranges ])
    ranges = [ int(i) for i in ranges.split(',') ]

    nbSprings = 0
    for i in ranges:
        nbSprings += i
    nbKnowns = records.count('#')
    nbUnknowns = records.count('?')
    toFind = nbSprings - nbKnowns
    # print(records, ranges, toFind)

    if records.count('?') == len(records):
        holes = len(records) - toFind - (len(ranges)-1)

    sum += recordMatch(records, ranges, toFind)
    print(sum)
