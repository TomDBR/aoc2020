import math
with open("./13.txt", 'r') as f:
    data = f.read().splitlines()
timestamp, shuttles = int(data[0]), list(map(lambda x: int(x) if x != 'x' else 'x', data[1].split(',')))

def run(timestamp, bus_list):
    start_time = timestamp
    bus_list = list(filter(lambda x: x != 'x', bus_list))
    while True:
        for bus in bus_list:
            if timestamp % bus == 0:
                return (timestamp - start_time) * bus
        timestamp += 1
    return None

def run2(bus_list):
    filtered_shuttles = list(filter(lambda l: l[1] != 'x', [ tup for tup in enumerate(bus_list) ]))
    start_time, incr = 0, filtered_shuttles[0][1]
    while True:
        if start_time % incr == 0:
            for idx, bus in filtered_shuttles[1:]:
                if (start_time + idx) % bus != 0:
                    break
            else:
                return start_time
        start_time += incr
    return None

print("PART 1:", run(timestamp, shuttles))
print("PART 2:", run2(shuttles))
