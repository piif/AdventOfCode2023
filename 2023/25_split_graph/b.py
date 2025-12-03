#!/bin/env python3

sum = 0

file = 'sample_b.txt'
# file = 'data_b.txt'

for i, line in enumerate(open(file)):
    line = line.strip('\n')
    print("read " + line)


print(sum)