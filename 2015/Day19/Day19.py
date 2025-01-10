from collections import defaultdict
import re

i1, i2 = open("2015/Day19/in.txt").read().split("\n\n")
subs = defaultdict(set)
for row in i1.split("\n"):
    fr, to = row.split(" => ")
    subs[fr].add(to)
pattern = "|".join(subs.keys())

gen = set()
for match in re.finditer(pattern, i2):
    a, b = match.span()
    for sub in subs[match.group()]:
        ns = i2[:a] + sub + i2[b:]
        gen.add(ns)
print(f"part1: {len(gen)}")

