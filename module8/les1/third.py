import random

d = {
    'q1?': [['a', 'b', 'c', 'd'], 'a'],
    'q2?': [['a', 'b', 'c', 'd'], 'c'],
    'q3?': [['a', 'b', 'c', 'd'], 'b'],
    'q4?': [['a', 'b', 'c', 'd'], 'd'],
}

lq = random.sample(d.keys(), 3)
print(lq)

for i in lq:
    random.shuffle(d[i][0])
    print(f'({i}) answers:\n{d[i][0]}')