from collections import namedtuple, Counter, defaultdict, deque, OrderedDict, ChainMap

# person1 = tuple([1, 4, 5])
# print(person1)
# Person = namedtuple('Person', ['name', 'age'])
# person2 = Person('Masha', '18')
# person = Person('Mick', '23')
# print(person)
# print(person.__doc__)
# print(person2._asdict())
#
#
# quantity = dict(Counter(stroka))
# print(quantity)
stroka = 'kkslsajflkajflsfdskjfdfjldskf'
# d = {}
# for i in stroka:
#     if i not in d:
#         d[i] = 0
#     d[i] += 1

d = dict(OrderedDict())

for i in stroka:
    d[i] = 1
d['q'] = 2
print(d)


