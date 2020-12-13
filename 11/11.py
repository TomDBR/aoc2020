with open("./11.txt", 'r') as f:
    data = f.read().splitlines()
width, height = len(data[0]), len(data)
data = ''.join(data)

def apply_vector(pos: int, vector: tuple):
    x, y = pos % width + vector[0], int(pos / width) + vector[1]
    if x < 0 or y < 0 or x >= width or y >= height: # we moved to invalid position
        return None
    return y * width + x # back to actual pos in list
    
def get_adjacent(pos: int, seats: list, vectors: list):
    adj_seats = set([ apply_vector(pos, vector) for vector in vectors ])
    return list(filter(lambda x: x is not None, adj_seats))

def get_visible(pos: int, seats: list, vectors: list):
    visible_seats = set()
    for vector in vectors:
        offset = 1
        while (new_pos := apply_vector(pos, tuple([ i * offset for i in vector ]))) != None:
            if seats[new_pos] != '.':
                visible_seats.add(new_pos)
                break
            offset += 1
    return visible_seats

def run(seats: str, func: object, seat_cnt: int):
    vectors = [ (1,0), (-1, 0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1) ]
    fnc_results = { i: list(func(i, list(seats), vectors)) for i in range(len(data)) }
    changes_made = -1
    last = list(seats)
    while changes_made != 0:
        changes_made = 0
        cur = last.copy()
        for idx,seat in enumerate(last):
            if seat == '.': # ignore floor
                continue
            occ_seats = [ last[i] for i in fnc_results[idx] ]
            if seat == 'L' and occ_seats.count('#') == 0:
                cur[idx] = '#'
                changes_made += 1
            elif seat == '#' and occ_seats.count('#') >= seat_cnt:
                cur[idx] = 'L'
                changes_made += 1
        last = cur
    return last

occ = lambda x: x == '#'
print("PART 1: ", len(list(filter(occ, run(data, get_adjacent, 4)))))
print("PART 2: ", len(list(filter(occ, run(data, get_visible, 5)))))
