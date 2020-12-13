with open("./12.txt", 'r') as f:
    data = f.read().splitlines()

def rotate(pos: int, degrees: int, clockwise: bool):
    to_ccw = { 270: 90, 180: 180, 90: 270 }
    if clockwise:
        degrees = to_ccw[degrees]
    quadrant = int(degrees/90)
    if quadrant == 1:
        return (-pos[1], pos[0])
    elif quadrant == 2:
        return (-pos[0], -pos[1])
    elif quadrant == 3:
        return (pos[1], -pos[0])
    return None

cnst_to_vect = lambda op, vec, cnst: tuple([ op(cnst, i) for i in vec ]) # apply const to each el in vect
vect_to_vect = lambda op, vec1, vec2: tuple([ op(vec1[i], vec2[i]) for i in range(len(vec1)) ]) # 

def get_pos(start_direction: tuple, use_waypoint: bool):
    directions = { 'N': (0,1), 'S': (0,-1), 'E': (1,0), 'W': (-1,0) }
    add, multiply = lambda a,b: a+b, lambda a,b: a*b
    # if use_waypoint is True, the direction is actually the waypoint's position
    pos, direction = (0,0), start_direction

    for instruction in data:
        action, value = instruction[:1], int(instruction[1:])
        if action in "NSEW":
            tmp = cnst_to_vect(multiply, directions[action], value)
            if use_waypoint: # in this case we update the wp's position
                direction = vect_to_vect(add, direction, tmp)
            else: # else, update the ship's position
                pos = vect_to_vect(add, pos, tmp)
        elif action in "LR":
            direction = rotate(direction, value, action == 'R')
        else: # moving ship to waypoint, or to new direction, is the same operation
            pos = vect_to_vect(add, pos, cnst_to_vect(multiply, direction, value))
    return pos

p1 = get_pos((1,0), False)
print("PART 1:", p1, abs(p1[0]) + abs(p1[1]))
p2 = get_pos((10,1), True)
print("PART 2:", p2, abs(p2[0]) + abs(p2[1]))
