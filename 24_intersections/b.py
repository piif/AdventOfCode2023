#!/bin/env python3

# file = 'sample_a.txt'
# slot=(7,27)
file = 'data_a.txt'
slot=(200000000000000, 400000000000000)

'''
  / x=Vrx.t + Prx
R:| y=Vry.t + Pry
  \ z=Vrz.t + Prz
  
   / x=Vnx.t + Pnx
Hn:| y=Vny.t + Pny
   \ z=Vnz.t + Pnz

R inter Hn =t1, t2 :
 / Vrx.t1 + Prx = Vnx.t2 + Pnx
 | Vry.t1 + Pry = Vny.t2 + Pny
 \ Vrz.t1 + Prz = Vnz.t2 + Pnz
 t2 = Vrx.t1 + Prx - Pnx / Vnx
 (Vry.Vnx - Vny.Vrx) t1 = Prx.Vny - Pry.Vnx - Pnx.Vny + Pny.Vnx
 (Vrz.Vnx - Vnz.Vrx) t1 = Prx.Vnz - Prz.Vnx - Pnx.Vnz + Pnz.Vnx

=> (Prx.Vny - Pry.Vnx - Pnx.Vny + Pny.Vnx)(Vrz.Vnx - Vnz.Vrx) = (Prx.Vnz - Prz.Vnx - Pnx.Vnz + Pnz.Vnx)(Vry.Vnx - Vny.Vrx)
  Prx.Vrz.Vnx.Vny (- Prx.Vrx.Vny.Vnz) - Pry.Vrz.Vnx² + Pry.Vrx.Vnx.Vnz
- Vrz.Pnx.Vnx.Vny (+ Vrx.Pnx.Vny.Vnz) + Vrz.Pnx.Vnx² + Vrx.Pny.Vnx.Vnz
- Prx.Vry.Vnx.Vnz (+ Prx.Vrx.Vny.Vnz) + Prz.Vry.Vnx² + Prz.Vrx.Vnx.Vny
+ Vry.Pnx.Vnz.Vnx (- Vrx.Pnx.Vny.Vnz) - Vry.Pnz.Vnx² - Vrx.Pnz.Vnx.Vny = 0
<=>
+ Vrx.(Pny.Vnx.Vnz - Pnz.Vnx.Vny)
+ Vrz.(Pnx.Vnx² - Pnx.Vnx.Vny)
+ Vry.(Pnx.Vnz.Vnx - Pnz.Vnx² )
+ Prx.Vry.(-Vnx.Vnz)
+ Prx.Vrz.(Vnx.Vny)
+ Pry.Vrx.(Vnx.Vnz)
+ Pry.Vrz.(-Vnx²)
+ Prz.Vrx.(Vnx.Vny)
+ Prz.Vry.(Vnx²)
 = 0

Inconnues =
Vrx
Vry
Vrz
Prx.Vry
Prx.Vrz
Pry.Vrx
Pry.Vrz
Prz.Vrx
Prz.Vry
'''

class hailstone:
    def __init__(self, p, v):
        (self.x, self.y, self.z) = p
        (self.vx, self.vy, self.vz) = v
        # self.A = self.vy
        # self.B = -self.vx
        # self.C = self.vx * self.y - self.vy * self.x

    # def eq(self):
    #     return f"{self.A}x{'+' if self.B>=0 else ''}{self.B}y{'+' if self.C>=0 else ''}{self.C}=0"

    def __str__(self):
        return f'p=({self.x}, {self.y}, {self.z}),v=({self.vx}, {self.vy}, {self.vz})'

    def coefs(self):
        return [
            self.y*self.vx*self.vz - self.z*self.vx*self.vy,
            self.x*self.vx*self.vx - self.x*self.vx*self.vy,
            self.x*self.vz*self.vx - self.z*self.vx*self.vx ,
            -self.vx*self.vz,
            self.vx*self.vy,
            self.vx*self.vz,
            -self.vx*self.vx,
            self.vx*self.vy,
            self.vx*self.vx
        ]

    def inter(self, other):
        fracY = (other.vy * self.vx - self.vy * other.vx)
        fracZ = (other.vz * self.vx - self.vz * other.vx)
        if fracY == 0 or fracZ == 0:
            return (None, None, None, None, None)
        t1y = (self.vy*other.x - self.vx*other.y + self.vx*self.y - self.vy*self.x) / fracY
        t1z = (self.vz*other.x - self.vx*other.z + self.vx*self.z - self.vz*self.x) / fracZ
        if t1y != t1z:
            return (None, None, None, None, None)
        x = other.vx * t1y + other.x
        y = other.vy * t1y + other.y
        z = other.vz * t1y + other.z
        return (t1, t2, x, y, z)

def printM(matrix):
    print("[")
    for l in matrix:
        print("  ", l)
    print("]")

def gauss_resolution(m):
    size = len(m)  
    A = [ l + [ i ] for i,l in enumerate(m) ]
    for j in range(size):
        printM(A)

        p = j
        for i in range(j, size):
            if abs(A[i][j]) > abs(A[p][j]):
                p = i
        A[j], A[p] = A[p], A[j]
        print(j, p, "=>", A[p][j])
        if A[j][j] == 0:
            continue

        for i in range(j+1, size):
            mu = -A[i][j] / A[j][j]
            for k in range(size):
                A[i][k] += mu * A[j][k]
                if A[i][k] < 1e-10:
                    A[i][k] = 0

    # A est triangulaire supérieure, il faut résoudre des équations
    printM(A)

    X = [ 0 for i in range(size) ]
    for i in range(size-1, -1, -1):
        # C'est compliqué hein
        if A[i][i]== 0:
            X[i] = 0
        else:
            X[i] = 1/A[i][i] * ( A[i][size] - sum([ A[i][k]*X[k] for k in range(i+1, size) ]) )
    return X

hailstones = []
def parseInput():
    for i, line in enumerate(open(file)):
        line = line.strip('\n')
        # print("read " + line)
        (p, v) = line.split(' @ ')
        hailstones.append(hailstone([ int(i) for i in p.split(', ') ], [ int(i) for i in v.split(', ') ]))

    # for h in hailstones:
    #     print(h)

def inSlot(v):
    return v is not None and v >= slot[0] and v <= slot[1]

def countCollisions():
    sum = 0
    for i,h1 in enumerate(hailstones):
        for h2 in hailstones[i+1:]:
            (x, y, t1, t2) = h1.inter(h2)
            # print("inter", h1, h2, x, y, t1, t2, inSlot(x) and inSlot(y))
            if inSlot(x) and inSlot(y) and t1 >= 0 and t2 >= 0:
                sum += 1
    return sum

parseInput()

# print(gauss_resolution([
#     [  2, -1,  0 ],
#     [ -1,  2, -1 ],
#     [  0, -1,  2 ]
# ]))

matrix = []
for h in hailstones[:9]:
    matrix.append(h.coefs())

(Vrx, Vry, Vrz, PrxVry, PrxVrz, PryVrx, PryVrz, PrzVrx, PrzVry ) = gauss_resolution(matrix)
Prx = PrxVry/Vry
Pry = PryVrx/Vrx
Prz = PrzVrx/Vrx
rock = hailstone((Prx, Pry, Prz), (Vrx, Vry, Vrz))
print(rock)

for h in hailstones:
    (t1, t2, x, y, z) = h.inter(rock)
    print(t1, t2, x, y, z)
# for i in range(len(hailstones)-10):
#     print("?", i)
#     matrix = []
#     for h in hailstones[i:i+9]:
#         matrix.append(h.coefs())
#     r = gauss_resolution(matrix)
#     if r is not None:
#         print(r)
#         break

# secants = []
# for i,h1 in enumerate(hailstones):
#     for j, h2 in enumerate(hailstones[i+1:]):
#         (t1, t2, x, y, z) = h1.inter(h2)
#         if t1 is not None:
#             secants.append((i, j))
# print(secants)