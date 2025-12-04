from itertools import product

grid = [[c for c in line] for line in open("2025/Day4/example.txt").read().splitlines()]

def getrollcoords(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                yield row, col

def getadjcoords(row, col, grid):
    for dr, dc in filter(lambda x: x != (0,0), product(range(-1,2), repeat=2)):
        nrow, ncol = row + dr, col + dc
        if nrow >= 0 and nrow < len(grid) and ncol >= 0 and ncol < len(grid[0]):
            yield nrow, ncol

def isaccessible(row, col, grid):
    adjrolls = 0
    for nrow, ncol in getadjcoords(row, col, grid):
        if grid[nrow][ncol] == '@':
            adjrolls += 1
    return adjrolls < 4

# Part 1
accessible = 0
for row, col in getrollcoords(grid):
    if isaccessible(row, col, grid):
        accessible += 1
print(f"part1: {accessible}")

# Part 2
progressed = True
nremovedrolls = 0
while progressed:
    progressed = False
    for row, col in getrollcoords(grid):
        if isaccessible(row, col, grid):
            nremovedrolls += 1
            progressed = True
            grid[row][col] = '.'
print(f"part2: {nremovedrolls}")