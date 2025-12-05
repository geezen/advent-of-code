a, b = open("2025/Day5/in.txt").read().split("\n\n")
ranges = [tuple(map(int, r.split('-'))) for r in a.splitlines()]
ids = [int(i) for i in b.splitlines()]

# Part 1
fresh = 0
for id in ids:
    for range_ in ranges:
        if id >= range_[0] and id <= range_[1]:
            fresh += 1
            break
print(f"Part 1: {fresh}")

# Part 2
ranges.sort()
allfresh = 0
prevhigh = -1
for range_ in ranges:
    if range_[1] <= prevhigh: #fully overlapping range
        continue
    allfresh += range_[1] - range_[0] + 1
    if range_[0] <= prevhigh: #party overlapping range
        allfresh -= prevhigh - range_[0] + 1
    prevhigh = range_[1]
print(f"Part 2: {allfresh}")