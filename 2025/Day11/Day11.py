import re

outputs = {}
for line in open("2025/Day11/in.txt").readlines():
    li = list(re.findall(r"\w+", line))
    outputs[li[0]] = set(li[1:])

def pathsfrom(node):
    if node == 'out': return 1
    ans = 0
    for child in outputs[node]:
        ans += pathsfrom(child)
    return ans

print(pathsfrom('you'))