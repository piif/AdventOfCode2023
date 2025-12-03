#!/bin/env python3

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

hands = []

order = [ 'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J' ]
figures = [ [], [2], [2, 2], [3], [2, 3], [4], [5] ]

def score(hand):
    score = 0
    jokers = 0
    cards = []
    for card in hand:
        index = 13 - order.index(card)
        cards.append(index)
        score = score * 16 + index
        if card == 'J':
            jokers += 1
    cards.sort()
    print(score, cards, jokers)

    count = 0
    counts = []
    prev = None
    for card in cards:
        if card == 1:
            continue
        if card == prev:
            count += 1
        else:
            prev = card
            if count > 1:
                counts.append(count)
            count = 1
    if count > 1:
        counts.append(count)
    counts.sort()
    print(counts)
    if counts == [] and jokers > 0:
        counts= [ jokers+1 if jokers<5 else 5 ]
    elif counts != []:
        counts[-1] += jokers
    print(counts)

    figure = figures.index(counts)
    print(figure)
    score += figure * (1<<20)

    return score

f = open(file, 'r')
for line in f.readlines():
    print("read " + line)
    (hand, bid) = line.strip('\n').split()
    hands.append({ 'hand': hand, 'bid': int(bid), 'score': score(hand) })

hands = sorted(hands, key = lambda hand : hand['score'])
for i, hand in enumerate(hands):
    print(i, hand['score'], hand['bid'])
    sum += (i+1) * hand['bid']
print(sum)
