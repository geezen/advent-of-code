inp = open("2025/Day7/example.txt").read().splitlines()
nextbeams = [1 if c == 'S' else 0 for c in inp[0]]
splits = 0
for line in inp[1:]:
    currentbeams = nextbeams
    nextbeams = [0 for _ in range(len(inp[0]))]
    for i, count in enumerate(currentbeams):
        if count == 0: continue
        if line[i] == '^':
            nextbeams[i - 1] += count
            nextbeams[i + 1] += count
            splits += 1
        else:
            nextbeams[i] += count
print(f"Part 1: {splits}")
print(f"Part 2: {sum(nextbeams)}")