#!/bin/env python3

sum = 0

file = 'sample_a.txt'
# file = 'data_a.txt'

for i, line in enumerate(open(file)):
    line = line.strip('\n')
    print("read " + line)


print(sum)
