#!/bin/env python3
import fnmatch

# file = 'sample_a.txt'
file = 'data_a.txt'

cache = {}
def recordMatch(record, ranges, ind=0):
    def inner(record, ranges, ind):
        # print('| '*ind, "match", record, ranges)
        if len(ranges) == 0:
            if record.count('#') != 0:
                # print('| '*ind, "-> 0")
                return 0
            else:
                # print('| '*ind, "-> 1")
                return 1

        s = 0

        rg0 = ranges[0]
        ranges = ranges[1:]
        test = '#'*rg0 + ('' if len(ranges) == 0 else '.')
        remaining = sum(ranges) + len(ranges)
        for i in range(len(record) - (rg0 + remaining) + 1):
            # print('| '*ind, "test", ('.'*i + test), record[:(i+len(test))])
            suffix = '' if len(ranges) == 0 else '.'
            if fnmatch.fnmatch('.'*i + test, record[:(i+len(test))]):
                s += recordMatch(record[(i+len(test)):], ranges, ind+1)
        return s

    key = (record, tuple(ranges))
    if key in cache:
        return cache[key]
    result = inner(record, ranges, ind)
    cache[key] = result
    return result


f = open(file, 'r')
s = 0
for line in f.readlines():
    # print("read " + line)
    (record, ranges) = line.split()
    record = '?'.join([ record, record, record, record, record ])
    ranges = ','.join([ ranges, ranges, ranges, ranges, ranges ])
    ranges= [ int(i) for i in ranges.split(',') ]

    s += recordMatch(record, ranges)

print(s)
