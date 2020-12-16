from functools import reduce
between = lambda num, floor, ceil: num <= ceil and num >= floor
valid_num = lambda num, ranges: True in [ between(num, r[0], r[1]) for r in ranges ]
to_int = lambda val: int(val)

def parse_rules(rules_txt, my_ticket, other_tickets):
    to_range = lambda text: [ tuple(map(to_int, r.split('-'))) for r in text.split(' or ') ]
    read_tickets = lambda list_: list(map(lambda x: list(map(to_int, x.split(','))), list_))
    rules = { name: to_range(ranges) for name, ranges in [ rule.split(': ') for rule in rules_txt ] }
    return rules, read_tickets(my_ticket[1:])[0], read_tickets(other_tickets[1:])

def valid_rule(ticket, rule):
    name, ranges = rule
    for num in ticket:
        if not valid_num(num, ranges):
            return None
    return name

with open("./16.txt", 'r') as f:
    rules, my_ticket, tickets = parse_rules(*list(map(lambda x: x.splitlines(), f.read().split("\n\n"))))

count = [] 
for ticket in tickets.copy():
    for num in ticket:
        for rule, ranges in rules.items():
            if valid_num(num, ranges):
                break
        else:
            count.append(num)
            tickets.remove(ticket)

my_ticket_dict = {}
while len(rules) != 0:
    for idx, ticket in enumerate(zip(*tickets)):
        matched_rules = set(filter(lambda x: x is not None, [ valid_rule(ticket, r) for r in rules.items() ]))
        if len(matched_rules) == 1:
            my_ticket_dict[(rule := matched_rules.pop())] = my_ticket[idx]
            rules.pop(rule)
my_ticket_dict = dict(filter(lambda x: x[0].startswith("departure"), my_ticket_dict.items()))

print("PART 1:", sum(count))
print("PART 2:", reduce(lambda a,b: a*b, my_ticket_dict.values()))
