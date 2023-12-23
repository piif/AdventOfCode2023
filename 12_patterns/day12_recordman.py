#!/bin/env python3

def combos(cfg):
    if cfg == "":
        return [""]
    
    return [ x + y for x in ("#." if cfg[0] == "?" else cfg[0]) for y in combos(cfg[1:])]

total = 0

for i, line in enumerate(open(0)):
    cfg, runs = line.split()
    runs = list(map(int, runs.split(',')))
    print(cfg, runs)

    for test in combos(cfg):
        if runs == [len(block) for block in test.split(".") if block]:
            total += 1

    print(total)