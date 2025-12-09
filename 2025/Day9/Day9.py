from itertools import combinations

redtiles = [tuple(map(int, line.split(','))) for line in open("2025/Day9/in.txt")]
maxarea = 0
for tile1, tile2 in combinations(redtiles, 2):
    area = abs((tile1[0]-tile2[0]+1)*(tile1[1]-tile2[1]+1))
    maxarea = max(area, maxarea)
print(maxarea)