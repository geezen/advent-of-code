moves = [move for move in open("in.txt", "r").readline()]
dirs = {"^": (-1,0), ">": (0,1), "v": (1,0), "<": (0,-1)}

def deliver(moves):
    row = col = 0
    visited = {(row,col)}
    for move in moves:
        dr, dc = dirs[move]
        row += dr
        col += dc
        visited.add((row,col))
    return visited

# part1
print(len(deliver(moves)))

# part2
santamoves = moves[::2]
robomoves = moves[1::2]
all = deliver(santamoves) | deliver(robomoves)
print(len(all))