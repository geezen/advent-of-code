import re

strings = [line.strip() for line in open("in.txt", "r").readlines()]

# part1
nice = 0
for string in strings:
    if len(re.findall(r"[aeiou]", string)) < 3: continue
    if re.search(r"(\w)\1", string) == None: continue
    if re.search(r"ab|cd|pq|xy", string) != None: continue
    nice += 1
print(f"{nice=}")

# part2
nice = 0
for string in strings:
    if re.search(r"(\w{2}).*\1", string) == None: continue
    if re.search(r"(\w).\1", string) == None: continue
    nice += 1
print(f"{nice=}")