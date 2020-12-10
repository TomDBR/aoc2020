import more_itertools as mit

with open("./10.txt", 'r') as f:
    data = sorted([ 0 ] + list(map(lambda x: int(x), f.read().splitlines())))
data.append(max(data)+3)

joltages_differences = [ 0, 0, 0 ]
for idx,jolt in enumerate(data[1:]):
    joltages_differences[(jolt - data[idx]) - 1] += 1

part2 = 1
grouped = [ list(group) for group in mit.consecutive_groups(data) ]
for grp in list(filter(lambda x: len(x) > 2, grouped)):
    ln = len(grp) - 2
    m = 2**ln
    if ln > 2:
        m -= 1
    part2 = part2 * m
print("PART1: ", joltages_differences[0] * joltages_differences[2])
print("PART2: ", part2)
