from math import sqrt

INPUT_PATH = "2025/Day8/example.txt"
PART1_ITERATIONS = 10

boxes = [tuple(map(int, line.split(','))) for line in open(INPUT_PATH).readlines()]

links = []
for box1 in boxes:
    for box2 in boxes:
        if box1 >= box2: continue
        dist = sqrt(sum([(x - y) ** 2 for x, y in zip(box1, box2)]))
        links.append((dist, box1, box2))

links.sort()
iterations = 0
circuits = [{box} for box in boxes]
while len(circuits) > 1:
    iterations += 1
    dist, box1, box2 = links.pop(0)
    box1circuit = next(filter(lambda s: box1 in s, circuits))
    box2circuit = next(filter(lambda s: box2 in s, circuits))
    if box1circuit != box2circuit:
        box1circuit.update(box2circuit)
        circuits.remove(box2circuit)
    if iterations == PART1_ITERATIONS:
        circuits.sort(key=lambda s: -1*len(s))
        ans = 1
        for circuit in circuits[:3]:
            ans *= len(circuit)
        print(f"Part 1: {ans}")
print(f"Part 2: {box1[0] * box2[0]}")