def get_neighbors(coord):
    expand_coord = lambda c: [ [i,i+1,i-1] for i in c]
    return set(map(lambda x: tuple(x), filter(lambda x: x != coord, get_all_combinations(expand_coord(coord)))))

def get_all_combinations(coord):
    wrapArray = lambda x: [x] if type(x) != list else x
    if len(coord) == 1:
        return coord[0]
    else:
        coords, res = [], get_all_combinations(coord[1:])
        for i in coord[0]:
            [ coords.append([i] + wrapArray(x)) for x in res ]
    return coords

with open("./17.txt", 'r') as f:
    data = f.read().splitlines()

def simulate(ndimensions: int, cycles: int):
    dimension = {}
    for x, row in enumerate(data):
        for y, _ in list(filter(lambda x: x[1] != '.', enumerate(row))):
            dimension[tuple([x,y] + [0]*(ndimensions-2))] = True
    for _ in range(cycles):
        i_dimension = dict(filter(lambda cube: cube[1] is True, dimension.copy().items()))
        neighbors = set()
        for cube, cube_is_active in dict(filter(lambda cube: cube[1] is True, dimension.items())).items():
            [ neighbors.add(nb) for nb in list(filter(lambda nb: nb not in dimension, get_neighbors(cube))) ]
        for nb in neighbors: # neighbors that weren't in dimension yet!
            dimension[nb] = False
        for cube, cube_is_active in dimension.items():
            active_neighbors = list(filter(lambda x: tuple(x) in dimension and dimension[tuple(x)] is True, get_neighbors(list(cube))))
            if cube_is_active is True:
                i_dimension[cube] = True if len(active_neighbors) in [2, 3] else False
            else:
                if len(active_neighbors) == 3:
                    i_dimension[cube] = True
        dimension = i_dimension
    return dimension

print("PART 1:", len(list(filter(lambda x: x is True, simulate(ndimensions=3, cycles=6).values()))))
print("PART 2:", len(list(filter(lambda x: x is True, simulate(ndimensions=4, cycles=6).values()))))
