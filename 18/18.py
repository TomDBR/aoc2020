from functools import reduce
import re

operations = { '+': lambda a,b: a+b, '*': lambda a,b: a*b }
def parse_formula(formula):
    op_or_assign = lambda res,op,new_res: int(new_res) if not op else op(res, int(new_res))
    idx, result, operation = 0, 0, None
    while idx < len(formula):
        ch,idx = formula[idx], idx+1
        if ch.isnumeric() or ch == "(": # time for an operation or assignment
            if ch == "(": # parse subexpression
                ch,incr = parse_formula(formula[idx:])
                idx += incr
            result = op_or_assign(result, operation, ch)
        elif ch in [ '+', '*' ]: # find operation we'll be doing on the next value/subexpression
            operation = operations[ch]
        else: # this means ')'
            return result, idx # return result subexpression
    return result,idx

with open("./18.txt", 'r') as f:
    data = list(map(lambda x: x.replace(' ', ''), f.read().splitlines()))
expand = lambda x: x.replace('+', ' + ').replace('*', ' * ').split(' ')

def parse2(formula: list, op : chr):
    idx = 1
    while idx < len(formula):
        i1,i2,ch = idx-1, idx+1, formula[idx]
        if ch == op:
            min1, plus1 = [ formula[i] for i in [i1,i2] ]
            prefix = '('* min1.count('(')
            suffix = ')'* plus1.count(')')
            plus1, min1 = plus1.replace(')', ''), min1.replace('(', '')
            if min1.isnumeric() and plus1.isnumeric():
                formula[idx] = prefix + str(operations[op](int(min1), int(plus1))) + suffix
                formula[i1], formula[i2] = None, None
                formula = list(filter(lambda x: x is not None, formula))
                idx -= 2
        idx += 1
    return formula

def formula2(formula):
    while formula.isnumeric() is False:
        reg = re.findall(r"\([^\(]+?\)", formula)
        if len(reg) == 0:
            reg.append(formula)
        for r in reg:
            if r[1:-1].isnumeric():
                formula = formula.replace(r, r[1:-1])
            elif r.count('+') > 0: # do plusses first
                formula = formula.replace(r, ''.join(parse2(expand(r), '+')))
            else:
                formula = formula.replace(r, ''.join(parse2(expand(r), '*')))
        formula = formula.replace(' ', '')
    return int(formula)

print("PART 1:", reduce(operations['+'], list(map(lambda x: parse_formula(x)[0], data))))
print("PART 2:", reduce(operations['+'], list(map(lambda x: formula2(x), data))))
