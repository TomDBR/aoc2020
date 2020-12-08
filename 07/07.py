with open("./07.txt", 'r') as f:
    data = f.read().splitlines()

rules = {}
for rule in data:
    rule = rule.replace(" bags", "").replace(" bag", "").replace(".", "")
    outer_bag, inner_bags = list(filter(lambda l: l.strip(), rule.split("contain")))
    inner_bags = list(map(lambda l: tuple(l.strip().split(' ', 1)), inner_bags.split(",")))
    rules[outer_bag.strip()] = { el[1]: int(el[0]) if el[0] != 'no' else 0 for el in inner_bags }

def check_bag(bag):
    eventual = []
    if len(rules[bag]) == 0 or 'other' in rules[bag]:
        return False
    if 'shiny gold' in rules[bag]:
        return True
    for k in rules[bag]:
        eventual.append(check_bag(k))
    return True in eventual

def count_bags(bag):
    count = 1
    if len(rules[bag]) == 0 or 'other' in rules[bag]:
        return 1
    for k,v in rules[bag].items():
        count += v * count_bags(k)
    return count

golden_bags = set()
for k,v in rules.items():
    if check_bag(k) is True:
        golden_bags.add(k)

print('PART 1: ', len(golden_bags))
print('PART 2: ', count_bags('shiny gold') - 1)
