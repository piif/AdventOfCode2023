#!/bin/env python3

# file = 'sample_a.txt'
file = 'data_a.txt'

f = open(file, 'r')
for line in f.readlines():
    (records, ranges) = line.split()
    records = '?'.join([ records, records, records, records, records ])
    ranges = ','.join([ ranges, ranges, ranges, ranges, ranges ])

    print(records, ranges)
