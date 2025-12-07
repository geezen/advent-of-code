inp = open("2025/Day7/in.txt").read().splitlines()
nextbeams = {inp[0].index('S')}
splits = 0
for line in inp[1:]:
    currentbeams = nextbeams
    nextbeams = set()
    for beam in currentbeams:
        if line[beam] == '^':
            nextbeams.add(beam - 1)
            nextbeams.add(beam + 1)
            splits += 1
        else:
            nextbeams.add(beam)
print(splits)