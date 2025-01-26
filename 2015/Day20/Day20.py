from collections import Counter
import math

inp = int(open("2015/Day20/in.txt").read())

def siv1(sivsize):
    arr = [0 for _ in range(sivsize)]
    for i in range(1,sivsize + 1):
        presents = 10 * i
        j = i
        while j < sivsize:
            arr[j] += presents
            j += i
    return arr

def siv2(sivsize):
    arr = [0 for _ in range(sivsize)]
    for i in range(1,sivsize + 1):
        presents = 11 * i
        j = i
        for _ in range(50):
            if j >= len(arr): break
            arr[j] += presents
            j += i
    return arr

size = 2
while True:
    cmax = 0
    for house, presents in enumerate(siv1(size)):
        if presents >= inp:
            print(f"part1: house {house} has {presents} presents")
            break
        cmax = max(cmax, presents)
    else:
        print(f"siv size {size} found max {cmax}")
        #print(siv(size))
        size *= 2
        continue
    break

size = 2
while True:
    cmax = 0
    for house, presents in enumerate(siv2(size)):
        if presents >= inp:
            print(f"part2: house {house} has {presents} presents")
            break
        cmax = max(cmax, presents)
    else:
        print(f"siv size {size} found max {cmax}")
        #print(siv(size))
        size *= 2
        continue
    break