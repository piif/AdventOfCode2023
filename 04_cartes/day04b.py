#!/bin/env python3

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

deck = []

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
            score += 1
    deck.append({ 'score': score, 'copies': 1 })
    # print(score)

print(deck)
for i in range(0, len(deck)):
    for j in range(1, deck[i]['score']+1):
        if i+j < len(deck):
            deck[i+j]['copies'] += deck[i]['copies']
print(deck)

for i in range(0, len(deck)):
    sum += deck[i]['copies'] # * (1 << (deck[i]['score']-1) if deck[i]['score'] != 0 else 0)
print(sum)
