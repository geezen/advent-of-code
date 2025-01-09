ingredients = {}
for line in open("2015/Day15/in.txt").readlines():
    name, rest = line.split(": ")
    props = {}
    for prop in rest.split(", "):
        k, v = prop.split()
        props[k] = int(v)
    ingredients[name] = props
ingredientnames = list(ingredients.keys())

def tbspdists(remtbsp, n):
    if n == 1:
        return [[remtbsp]]
    res = []
    for i in range(remtbsp + 1):
        prefix = [i]
        for rest in tbspdists(remtbsp - i, n - 1):
            res.append(prefix + rest)
    return res

def caldists(tcals):
    res = []
    for dist in tbspdists(100, len(ingredients)):
        distcals = 0
        for index, tbsp in enumerate(dist):
            distcals += ingredients[ingredientnames[index]]["calories"] * tbsp
        if distcals == tcals:
            res.append(dist)
    return res

def getscore(dist):
    score = 1
    for prop in ["capacity", "durability", "flavor", "texture"]:
        pv = 0
        for i, ingredient in enumerate(ingredients):
            pv += dist[i]*ingredients[ingredient][prop]
        score *= max(0, pv)
    return score

def gethiscore(dists):
    hiscore = 0
    for dist in dists:
        hiscore = max(hiscore, getscore(dist))
    return hiscore

print(f"part1: {gethiscore(tbspdists(100, len(ingredients)))}")
print(f"part2: {gethiscore(caldists(500))}")
