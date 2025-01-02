import re

def hasstraight(s):
    for i in range(len(s)-2):
        if ord(s[i]) == ord(s[i+1]) - 1 and ord(s[i+1]) == ord(s[i+2]) - 1:
            return True
    return False

def hasvalidletters(s):
    return re.match(r"^[^iol]*$",s) != None

def haspairs(s):
    return len(set(map(lambda t: t[0], re.findall(r"((\w)\2)", s)))) >= 2

def validate(pw):
    return hasstraight(pw) and hasvalidletters(pw) and haspairs(pw)
    
def nextpw(pw):
    pwlist = [ord(c) for c in pw]
    while True:
        pwlist[-1] += 1
        for i in range(len(pwlist) - 1, 0, -1):
            if pwlist[i] > ord("z"):
                pwlist[i-1] += 1
                pwlist[i] = ord("a")
        yield "".join(chr(i) for i in pwlist)

for pw in nextpw(open("2015/Day11/in.txt").readline()):
    if validate(pw):
        print(pw)