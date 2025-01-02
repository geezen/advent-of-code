import re

dists = {}
locations = set()
lines = [line.strip() for line in open("2015/Day9/in.txt").readlines()]

for line in lines:
    loc1, _, loc2, dist = re.findall("\w+", line)
    locations.update((loc1, loc2))
    dist = int(dist)
    dists[(loc1,loc2)] = dist
    dists[(loc2,loc1)] = dist

def maxrout(loc1, locs):
    if len(locs) == 1:
        return dists[(loc1,list(locs)[0])]
    maxr = 0
    for loc2 in locs:
        maxr = max(maxr, dists[(loc1,loc2)] + maxrout(loc2, locs - {loc2}))
    return maxr

ans = 0
for loc1 in locations:
    ans = max(ans, maxrout(loc1, locations - {loc1}))
print(ans)