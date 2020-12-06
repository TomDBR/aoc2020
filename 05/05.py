from functools import reduce

# OLD solution

#with open("./05.txt", 'r') as f:
##with open("/home/Tom/Downloads/p3hsbf", 'r') as f:
#    data = f.read().splitlines()
#
## contains tuples with: ( idx in range, increment/decrement sign )
#parse_dict = { 'F': (1,-1), 'B': (0,1), 'R': (0,1), 'L': (1,-1) }
#split_idx, pass_sz = max(data[0].rfind('F'), data[0].rfind('B')) + 1, len(data[0])
#
#def parse(code):
#    bit = 2 ** len(code) # value used for binary partitioning
#    code_range = [ 0, bit-1 ]
#    for range_idx, incr_sign in map(lambda l: parse_dict[l], code):
#        code_range[range_idx] += ( incr_sign * (bit := bit >> 1) )
#    return code_range[0] # both values in the range are the same now
#
#def get_seat_id(boarding_pass):
#    row, seat = [ boarding_pass[i:j] for i,j in zip([0,split_idx], [split_idx,pass_sz]) ]
#    return int(2 ** len(seat) * parse(row) + parse(seat))
#
#seats, max_sid = set(), 0
#for pass_ in data:
#    seats.add(sid := get_seat_id(pass_))
#    if sid > max_sid: 
#        max_sid = sid
#
#missing_seats = list(map(lambda x: x + 1, filter(lambda l: l+1 not in seats, range(max_sid - len(seats), max_sid))))
#print(f'part 1: {max_sid}\npart 2: {missing_seats}')

char_to_binary = { 'F': 0, 'B': 1, 'L': 0, 'R': 1 }
#with open("/home/Tom/Downloads/p3hsbf", 'r') as f:
with open("./05.txt", 'r') as f:
    data = list(map(lambda string: list(map(lambda ch: char_to_binary[ch], string)), f.read().splitlines()))

seats, max_sid = set(), 0
for pass_ in data:
    seats.add(sid := reduce(lambda total, bit: total << 1 | bit, pass_))
    if sid > max_sid:
        max_sid = sid
missing_seats = list(map(lambda x: x + 1, filter(lambda l: l+1 not in seats, range(max_sid - len(seats), max_sid))))
print(f'part 1: {max_sid}\npart 2: {missing_seats}')
