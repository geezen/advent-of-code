grid = [[c == "#" for c in line.strip()] for line in open("2015/Day18/in.txt").readlines()]
h = len(grid)
w = len(grid[0])

def adj8():
    z1 = 0 + 1j
    z2 = -1 + 1j
    for i in range(4):
        yield int(z1.real), int(z1.imag)
        yield int(z2.real), int(z2.imag)
        z1 *= 0+1j
        z2 *= 0+1j

tempgrid = [[False for _ in range(w)] for _ in range(h)]
for i in range(100):
    for cr in range(h):
        for cc in range(w):
            n_on = 0
            for dr,dc in adj8():
                nr = cr + dr
                nc = cc + dc
                if nr in range(h) and nc in range(w):
                    if grid[nr][nc]: n_on += 1
            if grid[cr][cc]:
                tempgrid[cr][cc] = n_on == 2 or n_on == 3
            else:
                tempgrid[cr][cc] = n_on == 3
    grid, tempgrid = tempgrid, grid
    
print(sum([sum(row) for row in grid]))