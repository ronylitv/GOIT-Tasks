import collections
from datetime import datetime
from collections import defaultdict


days_of_week = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

user_list = [
    {'Mike': datetime(year=1997, month=10, day=3)},
    {'Olesya': datetime(year=1978, month=8, day=24)},
    {'Nikita': datetime(year=2000, month=5, day=10)},
    {'Orest': datetime(year=2002, month=8, day=11)},
    {'Danylo': datetime(year=2002, month=8, day=1)},
    {'Natalya': datetime(year=1976, month=9, day=3)},
    {'Roman': datetime(year=1978, month=10, day=16)},
    {'Bohdan': datetime(year=2007, month=7, day=23)},
    {'Rostyslav': datetime(year=2007, month=7, day=21)},
    {'Yulia': datetime(year=2007, month=7, day=22)},
]


def congratulate(users: list):
    a = defaultdict(list)
    for human in users:
        for ind, val in human.items():
            if 5 <= val.weekday() <= 6:
                a[0].append(ind)
            else:
                a[val.strftime('%B')].append(ind)
    print(a)
    s = sorted(a.items())
    for el in s:
        names_to_congratulate = ', '.join(el[1])
        print(f'{days_of_week[el[0]]}: {names_to_congratulate}')


congratulate(user_list)


