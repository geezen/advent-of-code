import re
from itertools import product

machines = []
for line in open("2025/Day10/in.txt"):
    lights, buttons, jotalge =  re.findall(r"\[.*\]|\(.*\)|{.*}", line)
    lights = [c == '#' for c in lights[1:-1]]
    buttons = [tuple(map(int, re.findall(r"\d+", btn))) for btn in buttons.split(" ")]
    jotalge = tuple(map(int, re.findall(r"\d+", jotalge)))
    machines.append((lights, buttons, jotalge))

def applypresses(length, btnpresses):
    lights = [False for _ in range(length)]
    for btnpress in btnpresses:
        for light in btnpress:
            lights[light] = not lights[light]
    return lights

ans = 0    
for tlights, buttons, jotalge in machines:
    depth = 1
    while True:
        for btnpress in product(buttons, repeat=depth):
            nlights = applypresses(len(tlights), btnpress)
            if nlights == tlights:
                ans += depth
                break
        else:
            depth += 1
            continue
        break
print(ans)