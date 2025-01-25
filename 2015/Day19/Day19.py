from collections import defaultdict
import heapq, math, re

i1, i2 = open("2015/Day19/in.txt").read().split("\n\n")
subs = defaultdict(set)
for row in i1.split("\n"):
    fr, to = row.split(" => ")
    subs[fr].add(to)
pattern = "|".join(subs.keys())

def nextmolecules(curmol):
    gen = set()
    for match in re.finditer(pattern, curmol):
        a, b = match.span()
        for sub in subs[match.group()]:
            ns = curmol[:a] + sub + curmol[b:]
            gen.add(ns)
    return gen

def lenprefixmatch(s1, s2):
    for i, (c1, c2) in enumerate(zip(s1,s2)):
        if c1 != c2: break
    else:
        i += 1
    return i

print(f"part1: {len(nextmolecules(i2))}")

invsubs = {}
for k, v in subs.items():
    for nk in v:
        assert nk not in invsubs
        invsubs[nk] = k
invkeys = sorted(invsubs.keys(), key=lambda s: -1 * len(s))

def recfunc(curmol, depth):
    if curmol == "e": 
        return depth
    for key in invkeys:
        if match := re.search(key, curmol):
            a, b = match.span()
            nmol = curmol[:a] + invsubs[match.group()] + curmol[b:]
            res = recfunc(nmol, depth + 1)
            if res > 0: return res
    return -1

print(f"part2: {recfunc(i2, 0)}")