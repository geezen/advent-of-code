from collections import Counter

inp = open("2025/Day7/in.txt").read().splitlines()
nextbeams = [1 if i == inp[0].index('S') else 0 for i in range(len(inp[0]))]
for line in inp[1:]:
    currentbeams = nextbeams
    nextbeams = [0 for _ in range(len(inp[0]))]
    for i, count in enumerate(currentbeams):
        if line[i] == '^':
            nextbeams[i - 1] += count
            nextbeams[i + 1] += count
        else:
            nextbeams[i] += count
print(sum(nextbeams))