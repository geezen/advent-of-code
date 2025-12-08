import re
import heapq
from math import sqrt
from collections import defaultdict

INPUT_PATH = "2025/Day8/in.txt"
PART1_ITERATIONS = 1000

boxes = [tuple(map(int, re.findall(r"\d+", line))) for line in open(INPUT_PATH).readlines()]
links = []
for box1 in boxes:
    for box2 in boxes:
        if box1 >= box2: continue
        dist = sqrt(sum([(x - y) ** 2 for x, y in zip(box1, box2)]))
        links.append((dist, box1, box2))

heapq.heapify(links)
iterations = 0
circuits = [{box} for box in boxes]
while len(circuits) > 1:
    iterations += 1
    dist, box1, box2 = heapq.heappop(links)
    box1circuit = list(filter(lambda s: box1 in s, circuits))[0]
    box2circuit = list(filter(lambda s: box2 in s, circuits))[0]
    if box1circuit != box2circuit:
        box1circuit.update(box2circuit)
        circuits.remove(box2circuit)
    if iterations == PART1_ITERATIONS:
        circuits.sort(key=lambda s: -1*len(s))
        ans = 1
        for circuit in circuits[0:3]:
            print(len(circuit))
            ans *= len(circuit)
        print(f"Part 1: {ans}")
print(f"Part 2: {box1[0] * box2[0]}")