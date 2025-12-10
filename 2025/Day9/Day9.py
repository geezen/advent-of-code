from itertools import combinations
from pprint import pprint

# Part 1
redtiles = [tuple(map(int, line.split(','))) for line in open("2025/Day9/in.txt")]
maxarea = 0
for tile1, tile2 in combinations(redtiles, 2):
    area = abs((tile1[0]-tile2[0]+1)*(tile1[1]-tile2[1]+1))
    maxarea = max(area, maxarea)
print(maxarea)

# Part 2
xvals, yvals = {0}, {0}
for tile in redtiles:
    xvals.add(tile[0])
    yvals.add(tile[1])
xvals = sorted(xvals)
yvals = sorted(yvals)
xcordmap = {val: i for i, val in enumerate(xvals)}
ycordmap = {val: i for i, val in enumerate(yvals)}
grid = [[0 for _ in range(len(yvals) + 1)] for _ in range((len(xvals) + 1))]
for tile1, tile2 in zip(redtiles, redtiles[1:]+redtiles[:1]):
    #print(f"connecting {tile1=} w {tile2=}")
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

q = [(0,0)]
while q:
    x, y = q.pop(0)
    if grid[x][y] == 0:
        grid[x][y] = 3
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                q.append((nx, ny))
for tile in redtiles:
    x = xcordmap[tile[0]]
    y = ycordmap[tile[1]]
    grid[x][y] = 4

maxarea = 0
for tile1, tile2 in combinations(redtiles, 2):
    gxmin, gxmax = tuple(sorted(map(lambda x: xcordmap[x], [tile1[0], tile2[0]])))
    gymin, gymax = tuple(sorted(map(lambda x: ycordmap[x], [tile1[1], tile2[1]])))
    for x in range(gxmin, gxmax + 1):
        for y in range(gymin, gymax + 1):
            if grid[x][y] == 3:
                break
        else:
            continue
        break
    else:
        area = abs((tile1[0]-tile2[0]+1)*(tile1[1]-tile2[1]+1))
        if area >= maxarea:
            #print(f"new maxarea of {area} with {tile1} and {tile2}")
            maxtile1, maxtile2 = tile1, tile2
            maxarea = area
maxgx = set(map(lambda x: xcordmap[x], [maxtile1[0], maxtile2[0]]))
maxgy = set(map(lambda x: ycordmap[x], [maxtile1[1], maxtile2[1]]))
for x in range(len(grid)):
    for y in range(len(grid[0])):
        """if x in maxgx and y in maxgy:
            print("@", end="")
            continue"""
        print(grid[x][y], end="")
    print("")
print(maxarea)

# inte 1351587876