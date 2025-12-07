from functools import reduce
from operator import add, mul

lines = open("2025/Day6/example.txt").read().splitlines()
operators = {'+': add, '*': mul}

# Part 1
grid = [line.split() for line in lines]
accumulator = [1 if i == '*' else 0 for i in grid[-1]]
for row in grid[:-1]:
    for i, el in enumerate(row):
        if grid[-1][i] == '*':
            accumulator[i] *= int(el)
        else:
            accumulator[i] += int(el)
print(f"Part 1: {sum(accumulator)}")

# Part 2
inv_grid = []
sum = 0
for i in reversed(range(len(lines[0]))):
    s = ""
    for j in range(len(lines)):
        s += lines[j][i]
    if not s.isspace():
        inv_grid.append(s)
nbrs = []
for line in inv_grid:
    nbrs.append(int(line[:-1]))
    if line[-1] != ' ':
        sum += reduce(operators[line[-1]], nbrs)
        nbrs = []
print(f"Part 2: {sum}")