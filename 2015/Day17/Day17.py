from itertools import combinations

containers = [int(s) for s in open("2015/Day17/in.txt").readlines()]

part1 = 0
part2 = 0
part2done = False
for r in range(len(containers)):
    for comb in combinations(containers, r + 1):
        if sum(comb) == 150:
            part1 += 1
            if not part2done:
                part2 += 1
    part2done = part2 > 0
print(f"{part1=}")
print(f"{part2=}")