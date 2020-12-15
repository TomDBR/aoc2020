from functools import reduce
from collections import defaultdict

def memory(count: int, start_numbers: list):
    numbers = defaultdict(lambda: tuple(2 * [None]), { el: (idx,None ) for idx,el in enumerate(start_numbers) })
    last = start_numbers[-1]
    for idx in range(len(numbers), count):
        last = 0 if None in numbers[last] else reduce(lambda a,b:a-b, numbers[last])
        numbers[last] = ( idx, numbers[last][0] )
    print(f"For starting numbers: {start_numbers}, the {count}th number is: {last}")
[ memory(count, [8,0,17,4,1,12]) for count in [ 2020, 30000000 ] ]
