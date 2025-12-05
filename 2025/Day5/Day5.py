a, b = open("2025/Day5/example.txt").read().split("\n\n")
ranges = [tuple(map(int, r.split('-'))) for r in a.splitlines()]
ids = [int(i) for i in b.splitlines()]

fresh = 0
for id in ids:
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            fresh += 1
            break
print(fresh)