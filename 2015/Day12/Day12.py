import re
import json

def part1(s):
    return sum(map(int, re.findall("-?\d+", s)))

inp = open("2015/Day12/in.txt").readline()
print("part1: " + str(part1(inp)))

def part2(obj):
    if type(obj) == int: return obj
    if type(obj) == dict:
        res = 0
        for v in obj.values():
            if v == "red":
                return 0
            else:
                res += part2(v)
        return res
    if type(obj) == list:
        return(sum(part2(sub) for sub in obj))
    else:
        return 0

obj = json.loads(inp)
print("part2: " + str(part2(obj)))