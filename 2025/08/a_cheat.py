from __future__ import annotations
import os
import sys
import math
from dataclasses import dataclass
from collections import defaultdict
from itertools import combinations
from functools import reduce
from operator import mul

file_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

@dataclass
class JunctionBox:
    x: int
    y: int
    z: int

    @classmethod
    def from_string(cls, s: str) -> JunctionBox:
        x, y, z = list(map(int, s.split(",")))
        return cls(x, y, z)

    def calculate_distance_eucl(self, other: JunctionBox) -> float:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        # return math.sqrt(
        #     math.pow(self.x - other.x, 2)
        #     + math.pow(self.y - other.y, 2)
        #     + math.pow(self.z - other.z, 2)
        # )

    def __str__(self) -> str:
        return f"{self.x}/{self.y}/{self.z}"

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))


def calculate_distances(
    boxes: list[JunctionBox],
    sort: bool = True,
) -> dict[frozenset[JunctionBox], float]:
    distances: dict[frozenset[JunctionBox], float] = defaultdict(frozenset)

    for p, q in combinations(boxes, 2):
        # p, q are vectors of type JunctionBox
        distances[frozenset([p, q])] = p.calculate_distance_eucl(q)

    return sorted(distances, key=distances.get) if sort is True else distances


def connect(circuits: list[set[JunctionBox]], box_pair: list[JunctionBox]):
    connection_possibilities: list[set[JunctionBox]] = []
    for circuit in circuits:
        if box_pair & circuit != set():
            connection_possibilities.append(circuit)

    if len(connection_possibilities) == 0:
        circuits.append(box_pair)
    else:
        # we need to merge all the possibilities and the box pair into 1 big circuit
        merged = set()
        for item in connection_possibilities:
            circuits.remove(item)  # Remove the old, shorter circuits from the list too
            merged.update(item)

        merged.update(box_pair)

        circuits.append(merged)


if __name__ == "__main__":
    data = []
    for i, line in enumerate(open(sys.argv[1])):
        data.append(line.strip('\n'))

    junction_boxes = [JunctionBox.from_string(item) for item in data]
    distances = calculate_distances(junction_boxes, sort=True)

    for i, d in enumerate(distances):
        print(f"{i} : {d}")

    circuits: list[set[JunctionBox]] = []

    num_connections = 0
    for box_pair in distances:
        connect(circuits, box_pair)
        print(box_pair, " => ", circuits)

        num_connections += 1

        if num_connections == 10:
            print(
                "The product of the length of the 3 longest circuits is:",
                reduce(mul, sorted([len(c) for c in circuits], reverse=True)[:3]),
            )

        if len(circuits) == 1 and len(circuits[0]) == len(junction_boxes):
            print(
                "The product of the x coordinates of the junction box "
                f"that makes 1 big circuit is {list(box_pair)[0].x * list(box_pair)[1].x}"
            )
            break