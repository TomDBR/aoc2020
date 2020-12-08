with open("./08.txt", 'r') as f:
    instructions = list(map(lambda l: tuple(l.split(' ')), f.read().splitlines()))

def instruction_run(instr):
    visited = set()
    acc, pos = 0, 0
    while pos < len(instructions):
        op, arg = instr[pos]
        visited.add(pos)
        pos += 1 if op != 'jmp' else int(arg)
        if op == 'acc':
            acc += int(arg)
        if pos in visited:
            return False, acc
    return True, acc

def find_solution(instr):
    swap_instructions = lambda tup: ('nop' if tup[0] == 'jmp' else 'jmp', tup[1])
    nop_jmp_set = list(filter(lambda x: x[1][0] in [ 'nop', 'jmp' ], enumerate(instr)))
    instr_copy = instructions.copy()
    while True:
        run, reg = instruction_run(instr_copy)
        if run is True:
            return run, reg
        instr_copy = instructions.copy()
        idx,tup = nop_jmp_set.pop(0) # the index of jmp/nop instruction to swap, plus the opcode/arg itself
        instr_copy[idx] = swap_instructions(tup)

print("P1:", instruction_run(instructions))
print("P2:", find_solution(instructions))
