#!/bin/env python3

sum = 0

# file = 'sample_a.txt'
# slot=(7,27)
file = 'data_a.txt'
slot=(200000000000000, 400000000000000)

class hailstone:
    def __init__(self, p, v):
        (self.x, self.y, self.z) = [ int(i) for i in p.split(', ') ]
        (self.vx, self.vy, self.vz) = [ int(i) for i in v.split(', ') ]
        self.A = self.vy
        self.B = -self.vx
        self.C = self.vx * self.y - self.vy * self.x

    def eq(self):
        return f"{self.A}x{'+' if self.B>=0 else ''}{self.B}y{'+' if self.C>=0 else ''}{self.C}=0"

    def __str__(self):
        return f'p=({self.x}, {self.y}, {self.z}),v=({self.vx}, {self.vy}, {self.vz})'

    def inter(self, other):
        frac = self.A*other.B - other.A*self.B
        if frac == 0:
            return (None, None, None, None)
        y = (other.A*self.C - self.A*other.C) / frac
        x = (-self.B*y - self.C) / self.A
        t1 = (x-self.x)/self.vx
        t2 = (x-other.x)/other.vx
        return (x, y, t1, t2)

    def interSameT(self, other):
        if self.vx == other.vx:
            if self.x != other.x:
                return None # always false
            else:
                tx = None # always true
        else:
            tx = (other.x - self.x) / (self.vx - other.vx)
        if self.vy == other.vy:
            if self.y != other.y:
                return None # always false
            else:
                ty = None # always true
        else:
            ty = (other.y - self.y) / (self.vy - other.vy)
        if tx is None:
            return 0 if ty is None else ty
        elif ty is None:
            return tx
        else:
            return tx if tx == ty else None

hailstones = []
for i, line in enumerate(open(file)):
    line = line.strip('\n')
    # print("read " + line)
    (p, v) = line.split(' @ ')
    hailstones.append(hailstone(p, v))

for h in hailstones:
    print(h, h.eq())

def inSlot(v):
    return v is not None and v >= slot[0] and v <= slot[1]

for i,h1 in enumerate(hailstones):
    for h2 in hailstones[i+1:]:
        (x, y, t1, t2) = h1.inter(h2)
        # print("inter", h1, h2, x, y, t1, t2, inSlot(x) and inSlot(y))
        if inSlot(x) and inSlot(y) and t1 >= 0 and t2 >= 0:
            sum += 1

print(sum)
