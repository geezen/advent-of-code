from collections import defaultdict
import re

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

print(f"part1: {len(nextmolecules(i2))}")
