from functools import reduce
with open("./03.txt", 'r') as f: 
    data = f.read().splitlines()
x_size, y_size = len(data[0]), len(data)

def is_tree(pos):
    x, y = pos[0] % x_size, pos[1]
    return data[y][x] == '#'

def traverse_slope(slope):
    pos = (0,0)
    count = 0
    while pos[1] < y_size:
        if is_tree(pos):
            count += 1
        pos = (pos[0]+slope[0], pos[1]+slope[1])
    return count

print(f"PART 1: {traverse_slope((3,1))}")
print(f"PART 2: {reduce(lambda a,b: a * b, [ traverse_slope(s) for s in [ (1,1), (3,1), (5,1), (7,1), (1,2) ]])}")
