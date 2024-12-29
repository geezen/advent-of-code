inp = open("in.txt", "r").readline()

# Part 1
floor = 0
for c in inp:
    if c == "(": floor += 1
    if c == ")": floor -= 1

print(floor)

# Part 2
floor = 0
for i, c in enumerate(inp):
    if c == "(": floor += 1
    if c == ")": floor -= 1
    if floor < 0: break

print(i + 1)