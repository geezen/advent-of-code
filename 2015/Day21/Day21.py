import re
from itertools import combinations
from functools import reduce
from math import inf

raw = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""

class Fighter:
    def __init__(self, hp, damage, armor):
        self.hp = hp
        self.damage = damage
        self.armor = armor
    
    def isalive(self):
        return self.hp > 0
    
    def attack(self, other):
        adamage = max(self.damage - other.armor, 1)
        other.hp = max(other.hp - adamage, 0)

def parseitems(inp):
    res = []
    for line in inp.split("\n")[1:]:
        res.append(tuple(map(int, re.findall(r"(?<!\+)\d+", line))))
    return res

weapons, armors, rings = map(parseitems, raw.split("\n\n"))
bhp, bdamage, barmor = map(int, re.findall(r"\d+", open("2015/Day21/in.txt").read()))

def boughtitems():
    for weapon in weapons:
        for nbrarmor in range(2):
            for armor in combinations(armors, nbrarmor):
                for nbrrings in range(3):
                    for ring in combinations(rings, nbrrings):
                        yield weapon, *armor, *ring

def wins(mhp, mdamage, marmor):
    player = Fighter(mhp, mdamage, marmor)
    boss = Fighter(bhp, bdamage, barmor)
    attacker, target = player, boss
    while player.isalive() and boss.isalive():
        attacker.attack(target)
        attacker, target = target, attacker
    return player.hp > 0

mincost, maxcost = inf, 0
for citems in boughtitems():
    mhp = 100
    cost, mdamage, marmor = reduce(lambda a, b: tuple([c + d for c, d in zip(a, b)]), citems)
    if wins(mhp, mdamage, marmor):
        mincost = min(mincost, cost)
    else:
        maxcost = max(maxcost, cost)
        
print(f"part1: {mincost}")
print(f"part2: {maxcost}")