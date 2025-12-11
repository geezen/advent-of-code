import re
from functools import cache

outputs = {}
for line in open("2025/Day11/in.txt").readlines():
    li = list(re.findall(r"\w+", line))
    outputs[li[0]] = set(li[1:])

@cache
def pathlength(frm, to):
    if frm == to: return 1
    if frm not in outputs: return 0
    ans = 0
    for child in outputs[frm]:
        ans += pathlength(child, to)
    return ans

print(f"Part 1: {pathlength('you','out')}")

path1length = pathlength('svr', 'fft') * pathlength('fft', 'dac') * pathlength('dac', 'out')
path2length = pathlength('svr', 'dac') * pathlength('dac', 'fft') * pathlength('fft', 'out')
print(f"Part 2: {path1length + path2length}")