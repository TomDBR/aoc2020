with open("./09.txt", 'r') as f:
    data = list(map(lambda x: int(x), f.read().splitlines()))

def check_valid(idx, number, preamble_sz):
    if idx < preamble_sz:
        return
    sum_ = set()
    from_, to_ = idx - preamble_sz, idx
    for i in data[from_:to_]:
        sum_.add(i)
    for i in data[from_:to_]:
        if number - i in sum_:
            return True
    return False

def find_invalid_number(input_data, preamble_size):
    for idx,num in enumerate(data):
        if check_valid(idx, num, preamble_size) is False:
            return num

def find_contiguous_range(input_data, invalid_number):
    range_sum, range_ = input_data[0], [ input_data[0] ]
    for num in input_data[1:]:
        range_sum += num
        range_.append(num)
        while range_sum > invalid_number:
            range_sum -= range_.pop(0)
        if range_sum == invalid_number and len(range_) > 1: # make sure range isn't JUST the invalid number
            return min(range_) + max(range_)

invalid_number = find_invalid_number(data, 25)

print("P1: ", invalid_number)
print("P2: ", find_contiguous_range(data, invalid_number))
