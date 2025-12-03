#!/bin/env python3

import math

product = 1

# file = 'sample_a.txt'
file = 'data_a.txt'

def compute(time, distance):
    # D = Th*Tm = Th.(T-Th) = T.Th - Th² > Dmax
    # -Th² + TTh - Dmax > 0
    delta = time*time - 4*distance
    Thmin = (time - math.sqrt(delta)) / 2
    Thmax = (time + math.sqrt(delta)) / 2
    print(delta, Thmin, Thmax)
    if (Thmin == math.ceil(Thmin)):
        Thmin += 1
    if (Thmax == math.floor(Thmax)):
        Thmax -= 1
    res = int(math.floor(Thmax)-math.ceil(Thmin)+1)
    print(res)
    return res

f = open(file, 'r')
times = ''.join(f.readline().strip('\n').split(':')[1].split())
distances = ''.join(f.readline().strip('\n').split(':')[1].split())

print(compute(int(times), int(distances)))
