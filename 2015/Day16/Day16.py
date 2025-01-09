tt = {
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1
}

sues = {}
for line in open("2015/Day16/in.txt").readlines():
    s1, s2 = line.split(": ", 1)
    k = int(s1[4:])
    v = {}
    for prop in s2.split(", "):
        pn, pv = prop.split(": ")
        v[pn] = int(pv)
    sues[k] = v

for sue, props in sues.items():
    for pn, pv in props.items():
        if tt[pn] != pv:
            break
    else:
        print(f"part1: {sue}")
        break

for sue, props in sues.items():
    for pn, pv in props.items():
        if pn in ["cats", "trees"]:
            if tt[pn] >= pv:
                break
        elif pn in ["pomeranians", "goldfish"]:
            if tt[pn] <= pv:
                break
        else:
            if tt[pn] != pv:
                break
    else:
        print(f"part2: {sue}")
        break