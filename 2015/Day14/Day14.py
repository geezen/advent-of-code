import re
from collections import Counter

reindeers = []
for line in open("2015/Day14/in.txt").readlines():
    name = line.split(" ", maxsplit=1)[0]
    speed, runtime, resttime = map(int, re.findall("\d+", line))
    reindeers.append((name, speed, runtime, resttime))

def getdists(t):
    res = {}
    for name, speed, runtime, resttime in reindeers:
        k, r = divmod(t, runtime + resttime)
        if r >= runtime:
            dist = (k+1) * speed * runtime
        else:
            dist = (k * speed * runtime) + (r * speed)
        res[name] = dist
    return res

def getpoints(maxt):
    points = Counter()
    for t in range(1, maxt + 1):
        dists = getdists(t)
        maxdist = max(dists.values())
        for name, dist in dists.items():
            if dist == maxdist:
                points[name] += 1
    return points

print(f"part1: {max(getdists(2503).values())}")
print(f"part2: {max(getpoints(2503).values())}")