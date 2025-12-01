# Parse input to (direction, distance) touple
rotations = [(1, int(line[1:])) if line[0] == 'R' else (-1, int(line[1:])) for line in open("2025/Day1/in.txt").readlines()]

# Part 1
dial = 50
password = 0
for dir, dist in rotations:
    dial += dir * dist
    if dial % 100 == 0:
        password += 1

print(f"Part1: {password}")

# Part 2
dial = 50
password = 0
for dir, dist in rotations:
    for i in range(dist):
        dial += dir
        if dial % 100 == 0:
            password += 1

print(f"Part2: {password}")