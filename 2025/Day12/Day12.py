import re

inp = open("2025/Day12/in.txt").read().split("\n\n")
shapes = inp[:-1]
regions = [tuple(map(int, re.findall(r"\d+", line))) for line in inp[-1].splitlines()]

ans = 0
for region in regions:
    x = region[0] // 3
    y = region[1] // 3
    size = x * y
    boxes = sum(region[2:])
    if boxes <= size:
        ans += 1
print(ans)