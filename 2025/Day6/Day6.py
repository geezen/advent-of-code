input = [line.split() for line in open("2025/Day6/in.txt").readlines()]

# Part 1
accumulator = [1 if i == '*' else 0 for i in input[-1]]
for row in input[:-1]:
    for i, el in enumerate(row):
        if input[-1][i] == '*':
            accumulator[i] *= int(el)
        else:
            accumulator[i] += int(el)
print(sum(accumulator))