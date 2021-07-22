import collections
from collections import defaultdict, deque
import random
#
# d = deque()
# d.append('adsada')
# d.appendleft('adadad')
#
# d.append('lol')
# print(d)

Student = collections.namedtuple('Student', ['name', 'mark'])
NAMES = ['Orest', 'Rostyk', 'Vanya', 'Vlad', 'Sonia']
student_list = []
while True:
    student_list.append(Student(name=random.sample(NAMES, k=1), mark=random.randrange(1, 6)))
    symbol1 = input('Do u want to continue: ')
    if symbol1 != '+':
        continue
    else:
        print([(i.name, i.mark) for i in student_list if i[1] >= 4])
        break




