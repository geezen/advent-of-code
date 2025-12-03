import re

banks = [list(map(int, re.findall(r"\d", line))) for line in open("2025/Day3/in.txt").readlines()]

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