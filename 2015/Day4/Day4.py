from hashlib import md5

secret = open("in.txt", "r").readline()

def mine(n):
    target = "0" * n
    i = 1
    while True:
        s = (secret + str(i)).encode('utf-8')
        digest = md5(s).hexdigest()
        if digest[:n] == target: break
        i += 1
    return i, digest

print(f"part1 {mine(5)}")
print(f"part2 {mine(6)}")