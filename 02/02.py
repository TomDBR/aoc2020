import re
with open("./02.txt", 'r') as f: 
    data = list(map(lambda l: re.search(r'^(\d+)-(\d+) (.): (.*)$', l).groups(), f.read().splitlines()))
between = lambda x, mini, maxi: x >= int(mini) and x <= int(maxi)
#p1 = lambda min_,max_,ch,password: between(password.count(ch), min_, max_)
#p2 = lambda min_,max_,ch,password: len(list(filter(lambda f: f == True, [ password[x-1] == ch for x in [ int(min_), int(max_) ] ]))) == 1
#[ print(f"PART {i+1}: {len(list(filter(lambda x: l(*x), data)))} PASSWORDS") for i,l in enumerate([p1, p2]) ]

results = [0, 0]
for min_,max_,char,password in data:
    #min_, max_ = list(map(lambda l: int(l), occurence.split('-')))
    if between(password.count(char), min_, max_):
        results[0] += 1
    if len(list(filter(lambda f: f == True, [ password[int(x)-1] == char for x in [ min_, max_ ] ]))) == 1:
        results[1] +=1
[ print(f"PART {i+1}: {results[0]} passwords") for i,res in enumerate(results) ]
