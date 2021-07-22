import random

d = {
    'q1?': [['a', 'b', 'c', 'd'], 'a'],
    'q2?': [['a', 'b', 'c', 'd'], 'c'],
    'q3?': [['a', 'b', 'c', 'd'], 'b'],
    'q4?': [['a', 'b', 'c', 'd'], 'd'],
}

lq = random.sample(list(d.keys()), 3)
points = 0


for i in lq:
    random.shuffle(d[i][0])
    print(f'({i}) answers:\n{d[i][0]}')
    answer = str(input('Your answer: '))
    if answer == d[i][1]:
        print('Your answer is right!')
        points += 1
    else:
        print('Your answer isn`t right!')
print(f'Your score is: {points}/{len(lq)}')
