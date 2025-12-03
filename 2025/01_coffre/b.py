#!/bin/env python3

sum = 0

#file = 'sample_a.txt'
file = 'data_a.txt'

pos = 50

for i, line in enumerate(open(file)):
    line = line.strip('\n')
    if line == '':
        continue

    
    dir = line[0]
    move = int(line[1:])
    if dir == 'L':
        newpos = pos - move
    elif dir == 'R':
        newpos = pos + move
    else:
        raise Exception(f"Unexpected dir {dir}")
    delta = abs(newpos // 100)
    if delta > 0 and pos == 0:
        delta -= 1
    sum += delta
    pos = newpos % 100
    print(f"{i: 5}:{line:<5} ->{newpos // 100: 4} -> {pos: 3} => {sum}")

print(sum)
