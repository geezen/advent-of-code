import re

ranges = [tuple(map(int, range.split("-"))) for range in open("2025/Day2/in.txt").read().split(",")]

res1 = 0
res2 = 0
for ids in ranges:
    for id in range(ids[0], ids[1] + 1):
        s = str(id)
        if re.fullmatch(r"(\d+)\1", s):
            res1 += id
        if re.fullmatch(r"(\d+)\1+", s):
            res2 += id
print(f"part1: {res1}\npart2: {res2}")