import re
from functools import cache

inp = [line.strip() for line in open("in.txt").readlines()]
gates = {}
for line in inp:
    op = re.search("[A-Z]+", line)
    if op == None:
        x, t = re.findall("\w+|\d+", line)
        gates[t] = ("MOVE", x, "")
    elif op.group() == "NOT":
        op, x, t = re.findall("\w+|\d+", line)
        gates[t] = (op, x, "")
    else:
        x, op, y, t = re.findall("\w+|\d+", line)
        gates[t] = (op, x, y)

@cache
def wire(w):
    if w.isdigit():
        return int(w)
    op, x, y = gates[w]
    if op == "MOVE":
        return wire(x)
    elif op == "NOT":
        return ~wire(x)
    elif op == "AND":
        return wire(x) & wire(y)
    elif op == "OR":
        return wire(x) | wire(y)
    elif op == "LSHIFT":
        return wire(x) << wire(y)
    elif op == "RSHIFT":
        return wire(x) >> wire(y)
    else:
        assert False

aval = wire("a")
print(f"part1: {aval}")
wire.cache_clear()
gates["b"] = ("MOVE", str(aval), "")
aval = wire("a")
print(f"part2: {aval}")