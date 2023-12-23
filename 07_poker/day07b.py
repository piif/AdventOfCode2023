#!/bin/env python3

sum = 0

file = 'sample_b.txt'
# file = 'data_b.txt'

f = open(file, 'r')
for line in f.readlines():
    print("read " + line)


print(sum)