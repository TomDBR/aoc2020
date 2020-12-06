from functools import reduce
data = None
with open("./01.txt", 'r') as f:
    data = list(map(lambda l: int(l), f.read().splitlines()))
data.sort()

def get_result(data):
    iterations = 0
    #filtered = lambda l, vals: l[1] + reduce(lambda a,b: a+b, vals) <= 2020

    for idx1,num1 in enumerate(data):
        for idx2,num2 in list(filter(lambda l: l[1] + num1 <= 2020, enumerate(data))):
            for idx3,num3 in list(filter(lambda l: l[1] + num1 + num2 <= 2020, enumerate(data))):
                iterations += 1
                if len(set([idx1, idx2, idx3])) != 3:
                    continue
                if num1 + num2 + num3 == 2020:
                    print(f"({num1},{idx1}), ({num2},{idx2}), ({num3},{idx3}), = {num1 * num2 * num3}")
                    return iterations

print(get_result(data))
