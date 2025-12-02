import re

ranges = [tuple(map(int, range.split("-"))) for range in open("2025/Day2/in.txt").read().split(",")]

res = 0
for ids in ranges:
    for id in range(ids[0], ids[1] + 1):
        s = str(id)
        if re.fullmatch(r"(\d+)\1$", s):
            res += id
print(res)