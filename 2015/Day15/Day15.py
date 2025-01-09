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

def caldists(remcal, index):
    calsptbsp = ingredients[ingredientnames[index]]["calories"]
    if index == len(ingredientnames) - 1:
        if remcal % calsptbsp == 0:
            return [[remcal // calsptbsp]]
    res = []
    tbsps = 0
    while (ccals := tbsps * calsptbsp) <= remcal:
        prefix = [tbsps]
        for rest in caldists(remcal - ccals, index + 1):
            res.append(prefix + rest)
        tbsps += 1
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

#print(f"part1: {gethiscore(tbspdists(100, len(ingredients)))}")
dists = caldists(500, 0)
for dist in dists:
    distcals = 0
    for index, tbsp in enumerate(dist):
        distcals += ingredients[ingredientnames[index]]["calories"] * tbsp
    print(f"{distcals} cals in dist {dist}")
for ing in ingredientnames:
    print(f"{ing} calories: {ingredients[ing]['calories']}")
print(f"part2: {gethiscore(dists)}")
