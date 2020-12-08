with open("./06.txt", 'r') as f:
    data = list(map(lambda l: l.split('\n'), f.read()[:-1].split('\n\n')))

scores = [0,0]
for group in data:
    g_data = {}
    for ch in ''.join(group): # might as well concat the whole thing for a group together
        g_data[ch] = g_data.setdefault(ch, 0) + 1 # returns g_data[ch] if it's present, else 0
    scores[0] += len(g_data)
    scores[1] += len(dict(filter(lambda g: g[1] == len(group), g_data.items())))

[ print(f"PART {i+1}: {score}") for i,score in enumerate(scores) ]
