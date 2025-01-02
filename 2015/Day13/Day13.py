from itertools import permutations
from collections import defaultdict

hapscore = defaultdict(lambda: 0)
people = set()
for line in open("2015/Day13/in.txt").readlines():
    p1,_,sign,points,_,_,_,_,_,_,p2 = line.split()
    gain = int(points)
    if sign == "lose":
        gain *= -1
    p2 = p2[:-1]
    hapscore[p1,p2] = gain
    people.add(p1)

def gethap(perm):
    res = 0
    for i in range(len(perm) - 1):
        res += hapscore[perm[i], perm[i+1]]
        res += hapscore[perm[i+1], perm[i]]
    res += hapscore[perm[0], perm[-1]]
    res += hapscore[perm[-1], perm[0]]
    return res

max_ = 0
for perm in permutations(people):
    max_ = max(max_, gethap(perm))
print(f"part1: {max_}")

people.add("me")
max_ = 0
for perm in permutations(people):
    max_ = max(max_, gethap(perm))
print(f"part1: {max_}")