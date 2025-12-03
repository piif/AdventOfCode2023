#!/bin/env python3

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

f = open(file, 'r')
for line in f.readlines():
    print("read " + line)
    (card, sets)=line.split(': ')
    (wining, having)= sets.split(' | ')
    winings = wining.strip(' \n').split()
    havings = having.strip(' \n').split()
    # print(winings, havings)
    score = 0
    for h in havings:
        if h in winings:
            if score == 0:
                score = 1
            else:
                score *= 2
    # print(score)
    sum+= score

print(sum)
