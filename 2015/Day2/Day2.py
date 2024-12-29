import re

paper = 0
ribbon = 0
for line in open("in.txt", "r").readlines():
    l, w, h = map(int, re.findall("\d+", line))
    minside = min(l*w, w*h, h*l)
    paper += 2*l*w + 2*w*h + 2*h*l + minside
    minparim = min(l+w, w+h, h+l) * 2
    ribbon += minparim
    ribbon += l * w * h
print(f"{paper=}")
print(f"{ribbon=}")