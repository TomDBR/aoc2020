import re
from functools import reduce
with open("./14.txt", 'r') as f:
    data = f.read().splitlines()

mask, register = None, {}
for r in data:
    if r.startswith("mask"):
        mask = r.split(' = ')[1]
    else:
        reg_address, value = re.match(r'^mem\[(\d+)\] = (\d+)$', r).groups()
        val_binary = [ '1' if int(value) & (1 << (35-n)) else '0' for n in range(36) ]
        for idx,ch in enumerate(mask):
            if ch in [ '1', '0' ]:
                val_binary[idx] = ch
        register[int(reg_address)] = reduce(lambda total, bit: total << 1 | int(bit), list(map(lambda x: int(x), val_binary)))
print(reduce(lambda a,b: a+b, filter(lambda x: x != 0, register.values())))

def get_addresses(begin_idx: int, address: list, mask: str):
    addresses = set()
    for idx,ch in enumerate(mask[begin_idx:], begin_idx):
        if ch == 'X': 
            for el in [ '1', '0' ]:
                address[idx] = el
                [ addresses.add(addr) for addr in get_addresses(idx+1, address.copy(), mask) ]
    addresses.add(''.join(address))
    return addresses
    
mask, register = None, {}
for r in data:
    if r.startswith("mask"):
        mask = r.split(' = ')[1]
    else:
        reg_address, value = re.match(r'^mem\[(\d+)\] = (\d+)$', r).groups()
        address_binary = [ '1' if int(reg_address) & (1 << (35-n)) else '0' for n in range(36) ]
        for idx,ch in enumerate(mask):
            if ch == '1': address_binary[idx] = '1'
        for i in get_addresses(0, address_binary, mask):
            masked_val = reduce(lambda total, bit: total << 1 | int(bit), list(map(lambda x: int(x), i)))
            register[masked_val] = int(value)
print(reduce(lambda a,b: a+b, filter(lambda x: x != 0, register.values())))
