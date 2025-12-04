from itertools import product

grid = [[c for c in line] for line in open("2025/Day4/example.txt").read().splitlines()]

accessible = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] != '@': continue
        adjrolls = 0
        for dr, dc in filter(lambda x: x != (0,0), product(range(-1,2), repeat=2)):
            nrow, ncol = row + dr, col + dc
            if nrow < 0 or nrow >= len(grid) or ncol < 0 or ncol >= len(grid[0]): continue
            if grid[nrow][ncol] == '@':
                adjrolls += 1
        if adjrolls < 4:
            accessible += 1
print(f"part1: {accessible}")