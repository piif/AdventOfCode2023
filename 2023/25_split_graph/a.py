#!/bin/env python3
import random

sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

graph = {}
nodes = {}

def stack(src, dst):
    if src not in nodes:
        nodes[src] = None
    if src in graph:
        graph[src][dst] = 0
    else:
        graph[src] = { dst: 0 }

def parseFile():
    global graph, nodes
    for i, line in enumerate(open(file)):
        line = line.strip('\n')
        # print("read " + line)
        src, arcs = line.split(': ')
        for dst in arcs.split(' '):
            stack(src, dst)
            stack(dst, src)

    print(len(graph), "nodes")
    (maxA, sumA) = countArcs()
    print(sumA, "arcs", maxA, "max")

def countArcs():
    maxA=0
    sum=0
    for n, arcs in graph.items():
        maxA = max(maxA, len(arcs))
        sum+=len(arcs)
    return (maxA, sum//2)

def resetGraph(value = None):
    for k in nodes.keys():
        nodes[k] = value

def computeDistances(n1):
    tries = [ n1 ]
    step = 0
    while True:
        newTries = []
        for node in tries:
            nodes[node] = step
            for next in graph[node].keys():
                if nodes[next] is None:
                    newTries.append(next)
                    graph[node][next] += 1
        if len(newTries) == 0:
            break
        tries = newTries
        step += 1

def dijkstra(n1, n2):
    current = n1
    nodes[current] = (True, 0)
    iter = 0

    while True:
        iter += 1
        # print("iter", iter, current)
        (visited, currDistance) = nodes[current]
        nodes[current] = (True, currDistance)

        for node, count in graph[current].items():
            (visited, distance) = nodes[node]
            if visited:
                continue
            if currDistance + 1 < distance:
                nodes[node] = (visited, currDistance + 1)
            # if node == n2:
            #     return True

        minDistance = maxDist
        current = None
        for key, (visited, distance) in nodes.items():
            if not visited and distance < minDistance:
                current = key
                minDistance = distance
        if current is None:
            print("Problem ...")
            return False

def markPath(n1, n2):
    node = n1
    while node != n2:
        minDistance = maxDist
        next = None
        for key in graph[node].keys():
            (visited, distance) = nodes[key]
            if distance < minDistance:
                next = key
                minDistance = distance
        graph[node][next] += 1
        node = next

def printGraph():
    for src, distance in nodes.items():
        print(f'{src}[{distance}]:', end='')
        for dst, count in graph[src].items():
            print(f' {dst}[{count}]', end='')
        print()

parseFile()
maxDist = len(nodes)+1

# printGraph()

def findMostUsedArcs():
    for k in nodes.keys():
        computeDistances(k)
        resetGraph()

    # printGraph()

    arcs = {}
    def addArc(k, d):
        if k in arcs:
            arcs[k] += d
        else:
            arcs[k] = d

    for n in nodes.keys():
        for a,distance in graph[n].items():
            if a > n:
                addArc((n, a), distance)
            else:
                addArc((a, n), distance)

    return sorted([ (v, k) for k, v in arcs.items() ], reverse = True)
# print(arcList)

def tryCuts():
    cuts = 0
    for n, (src, dst) in arcList:
        del graph[src][dst]
        del graph[dst][src]
        cuts += 1
        computeDistances(src)
        others = list(nodes.values()).count(None)
        if others != 0:
            print(cuts, "=>", others, len(nodes)-others, others * len(nodes)-others)
            break
        resetGraph()

    for i, (n, (isrc, idst)) in enumerate(arcList[:cuts]):
        graph[isrc][idst] = 0
        graph[idst][isrc] = 0
    return cuts

def checkThreeCuts():
    src=list(nodes.keys())[-1]

    i = cuts-1
    while i >= 0:
        print("try", i, "...")
        ni, (isrc, idst) = arcList[i]
        del graph[isrc][idst]
        del graph[idst][isrc]
        j = i-1
        while j >= 0:
            nj, (jsrc, jdst) = arcList[j]
            del graph[jsrc][jdst]
            del graph[jdst][jsrc]
            k = j-1
            while k >= 0:
                nk, (ksrc, kdst) = arcList[k]
                # print("try", i, j, k)
                del graph[ksrc][kdst]
                del graph[kdst][ksrc]
                computeDistances(src)
                others = list(nodes.values()).count(None)
                if others != 0:
                    print("found", isrc, idst, jsrc, jdst, ksrc, kdst)
                    print("=>", others, len(nodes)-others, others * (len(nodes)-others))
                resetGraph()
                graph[ksrc][kdst] = 0
                graph[kdst][ksrc] = 0
                k -= 1
            graph[jsrc][jdst] = 0
            graph[jdst][jsrc] = 0
            j -= 1
        graph[isrc][idst] = 0
        graph[idst][isrc] = 0
        i -= 1

# arcList=findMostUsedArcs()
# cuts = tryCuts()
# checkThreeCuts()

# found tqn tvf krx lmg tnr vzb
# => 746 781 1138396
# -> your answer is too high ??

del graph['tqn']['tvf']
del graph['tvf']['tqn']
del graph['krx']['lmg']
del graph['lmg']['krx']
del graph['tnr']['vzb']
del graph['vzb']['tnr']

computeDistances('tqn')
others = list(nodes.values()).count(None)
print("tqn =>", others, len(nodes)-others, others * (len(nodes)-others))

resetGraph()
computeDistances('tvf')
others = list(nodes.values()).count(None)
print("tvf =>", others)

#     computeDistances(src)
#     others = list(nodes.values()).count(None)
#     if others == 0:
#         print(i, "must stay cut")
# (maxA, sumA) = countArcs()
# print(sumA, "arcs", maxA, "max")
