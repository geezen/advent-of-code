import re

grid = [[0 for _ in range(1000)] for _ in range(1000)]

cmds = {
    "turn off": lambda x: 0,
    "toggle": lambda x: x^1,
    "turn on": lambda x: 1
}

for line in open("in.txt", "r").readlines():
    cmd, x1, y1, x2, y2 = re.match(r"(turn off|toggle|turn on) (\d+),(\d+) through (\d+),(\d+)", line).group(*range(1,6))
    x1, y1, x2, y2 = map(int,(x1, y1, x2, y2))
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] = cmds[cmd](grid[x][y])

ans = 0
for row in grid:
    for el in row:
        ans += el
print(ans)