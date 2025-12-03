import re

banks = [list(map(int, re.findall(r"\d", line))) for line in open("2025/Day3/in.txt").readlines()]

# part1  
res = 0
for bank in banks:
    digit1_index = 0
    digit1_val = 0
    for i in range(len(bank) - 2, -1, -1):
        if bank[i] >= digit1_val:
            digit1_index = i
            digit1_val = bank[i]
    digit2_val = 0
    for i in range(digit1_index + 1, len(bank)):
        digit2_val = max(digit2_val, bank[i])
    res += 10*digit1_val + digit2_val
print(f"part1: {res}")

# part 2
def findjoltage(bank, nbats):
    joltage = 0
    prevdigit_index = -1
    for right in range(nbats, 0, -1):
        maxdigit_val = 0
        for i in range(prevdigit_index + 1, len(bank) - right + 1):
            if bank[i] > maxdigit_val:
                maxdigit_val = bank[i]
                prevdigit_index = i
        joltage *= 10
        joltage += maxdigit_val
    return joltage

res = 0
for bank in banks:
    res += findjoltage(bank, 12)
print(f"part2: {res}")