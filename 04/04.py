import re
import sys

four_digits, height = re.compile(r'^\d{4}$'), re.compile(r'^(\d+)([c,i][m,n])$')
height_metrics = { 'cm': (150,193), 'in': (59, 76) }
between = lambda val,lo,hi: lo <= val and hi >= val

validation_functions = {
        'byr': lambda val: re.match(four_digits, val) is not None and between(int(val), 1920, 2002),
        'iyr': lambda val: re.match(four_digits, val) is not None and between(int(val), 2010, 2020),
        'eyr': lambda val: re.match(four_digits, val) is not None and between(int(val), 2020, 2030), 
        'hgt': lambda val: val[-2:] in [ 'cm', 'in' ] and between(int(val[:-2]), *height_metrics[val[-2:]]),
        'hcl': lambda val: re.match(r'^(#)[0-9a-f]{6}$', val) is not None,
        'ecl': lambda val: val in [ 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' ],
        'cid': lambda val: True,
        'pid': lambda val: re.match(r'^\d{9}$', val) is not None
}

with open("./04.txt", 'r') as f:
    data = list(map(lambda x: x.replace('\n', ' ').split(' '), f.read()[:-1].split('\n\n')))
    passwords = list(map(lambda l: { x[0]: x[1] for x in [ el.split(':') for el in l ]}, data))

valid_p1, valid_p2 = 0, 0
for p in passwords:
    if len(p) == 8 or (len(p) == 7 and 'cid' not in p):
        valid_p1 += 1
        for field,value in p.items():
            if not validation_functions[field](value):
                break
        else:
            valid_p2 += 1
print(f"PART 1: {valid_p1} valid passwords.")
print(f"PART 2: {valid_p2} valid passwords.")
