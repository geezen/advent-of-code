import re

inp = open("2015/Day10/in.txt").readline()

def las(s):
    res = ""
    for run in map(lambda t: t[0], re.findall(r"((\d)\2*)", s)):
        res += str(len(run)) + run[0]
    return res

s = inp
for i in range(50):
    print(f"round {i} len {len(s)}")
    s = las(s)
print(f"final ans {len(s)}")
#TODO divide and conquor throug memoization