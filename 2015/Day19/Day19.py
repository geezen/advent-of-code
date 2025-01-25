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