import re

lines = open("in.txt").read().splitlines()

ans = 0
for line in lines:
    codesize = len(line)
    nline = re.sub(r"\\\\|\\x[0-9a-f]{2}|\\\"", "X", line)
    nline = nline[1:-1]
    charsize = len(nline)
    ans += codesize - charsize
print(f"part1: {ans}")

ans = 0
for line in lines:
    encstring = '"'
    for c in line:
        if c == '"':
            encstring += r"\""
        elif c == "\\":
            encstring += "\\\\"
        else:
            encstring += c
    encstring += '"'
    ans += len(encstring) - len(line)
print(f"part2: {ans}")