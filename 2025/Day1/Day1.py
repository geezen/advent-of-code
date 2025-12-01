dial = 50
password = 0

for line in open("2025/Day1/in.txt").readlines():
    sign = -1 if line[0] == 'L' else 1
    dist = int(line[1:])
    rotation = sign * dist
    dial += rotation
    if dial % 100 == 0:
        password += 1

print(f"Part1: {password}")