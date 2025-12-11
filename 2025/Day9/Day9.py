from itertools import combinations

# Part 1
redtiles = [tuple(map(int, line.split(','))) for line in open("2025/Day9/in.txt")]
maxarea = 0
for tile1, tile2 in combinations(redtiles, 2):
    area = abs((tile1[0]-tile2[0]+1)*(tile1[1]-tile2[1]+1))
    maxarea = max(area, maxarea)
print(f"Part 1: {maxarea}")

# Part 2
# Create compressed grid
xvals, yvals = {0}, {0}
for tile in redtiles:
    xvals.add(tile[0])
    yvals.add(tile[1])
xvals = sorted(xvals)
yvals = sorted(yvals)
xcordmap = {val: i for i, val in enumerate(xvals)}
ycordmap = {val: i for i, val in enumerate(yvals)}
grid = [[0 for _ in range(len(yvals) + 1)] for _ in range((len(xvals) + 1))]
# Connect tiles
for tile1, tile2 in zip(redtiles, redtiles[1:]+redtiles[:1]):
    xmin = min(tile1[0], tile2[0])
    xmax = max(tile1[0], tile2[0])
    gxmin = xcordmap[xmin]
    gxmax = xcordmap[xmax]
    ymin = min(tile1[1], tile2[1])
    ymax = max(tile1[1], tile2[1])
    gymin = ycordmap[ymin]
    gymax = ycordmap[ymax]
    if gxmin != gxmax:
        for gx in range(gxmin, gxmax + 1):
            grid[gx][ycordmap[tile1[1]]] = 1
    else:
        for gy in range(gymin, gymax + 1):
            grid[xcordmap[tile1[0]]][gy] = 1

# Floodfill outside
q = [(0,0)]
while q:
    x, y = q.pop(0)
    if grid[x][y] == 0:
        grid[x][y] = 2
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                q.append((nx, ny))

# Check area for all rectangles not containing unpainted tiles
maxarea = 0
for tile1, tile2 in combinations(redtiles, 2):
    gxmin, gxmax = tuple(sorted(map(lambda x: xcordmap[x], [tile1[0], tile2[0]])))
    gymin, gymax = tuple(sorted(map(lambda x: ycordmap[x], [tile1[1], tile2[1]])))
    for x in range(gxmin, gxmax + 1):
        for y in range(gymin, gymax + 1):
            if grid[x][y] == 2:
                break
        else:
            continue
        break
    else:
        area = (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)
        maxarea = max(maxarea, area)
print(f"Part 2: {maxarea}")