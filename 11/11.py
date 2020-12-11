def same_row(position, offset, comparator):
    row = int(position / width)
    comp_row = int(comparator / width)
    return comp_row + offset == row

def get_adjacent_seats(position, seats):
    adj = list(filter(lambda l: same_row(position, 0, l), [ position + 1, position -1 ]))
    for row_offset, new_position in [ (-1, position + width), (1, position - width) ]:
        tmp = [ new_position, new_position - 1, new_position + 1 ]
        adj.extend(list(filter(lambda l: same_row(position, row_offset, l), tmp)))
    return list(filter(lambda x: x >= 0 and x < width * height, adj))

def get_visible_seats(position, seats):
    between = lambda hi,lo,val: val >= lo and val < hi
    visible = []
    for diff in [ 1, -1 ]:
        offset = 1
        while between(len(seats), 0, (new_position := position + ( offset * diff))):
            if same_row(position, 0, new_position) and seats[new_position] != '.':
                visible.append(new_position)
                break
            offset += 1
    for diff in [ width, -width ]:
        offset = 1
        while between(len(seats), 0, (new_position := position + ( offset * diff))):
            if seats[new_position] != '.':
                visible.append(new_position)
                break
            offset += 1
    for of,diff in [ (1,width), (-1,-width), (1,-width), (-1,width) ]:
        offset = 1
        # this part is really BAD
        while between(len(seats), 0, (new_position := position + ( offset * diff) + ( offset * of))):
            tmps = - offset if new_position > position else offset
            if same_row(position, tmps, new_position):
                if seats[new_position] != '.':
                    visible.append(new_position)
                    break
            offset += 1
    return visible

def print_layout(seats):
    for idx,i in enumerate(seats):
        if idx > 0 and idx % width == 0:
            print()
        print(i, end='')
    print()


def run_environment(seats, relevant_seats_func, occupied_seats_count):
    last = list(seats)
    while True:
        state_count = 0
        cur = last.copy()
        for idx,seat in enumerate(last):
            if seat == '.': # ignore floor
                continue
            adj_seats = [ last[i] for i in relevant_seats_func(idx, last) ]
            if seat == 'L':
                if adj_seats.count('#') == 0:
                    cur[idx] = '#'
                    state_count += 1
            elif seat == '#':
                if adj_seats.count('#') >= occupied_seats_count:
                    cur[idx] = 'L'
                    state_count += 1
        last = cur
        if state_count == 0:
            break
    return last
    
with open("./11.txt", 'r') as f:
    data = f.read().splitlines()
width, height = len(data[0]), len(data)
data = ''.join(data)

occupied_seats = lambda x: x == '#'
print("PART 1: ", len(list(filter(occupied_seats, run_environment(list(data), get_adjacent_seats, 4)))))
print("PART 2: ", len(list(filter(occupied_seats, run_environment(list(data), get_visible_seats, 5)))))
