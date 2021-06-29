d = {1: 3, 2: 5}
# a = d.pop(1)
# print(d, a)

#
# l = [1, 2, 3]
# print(l.pop())
# a = d.copy()
# for i in d.copy():
#     if i == 1:
#         d.pop(1)
#
# print(d)
# print(a)

a = {3: 4, 4: 5}
d.update(a)
print(d)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
d = {}
for i, val in enumerate(l1):
    d[val] = l2[i]
print(d)
# Переробити
d = {'Math': 4, 'Ukrainian': 4, 'English': 5, 'Physic' : 5, 'Chemistry': 3}
marks = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

# b = 0
# for i in d.values():
#     marks[i] += 1
#     b += 1
#     res += i
#
# print(marks)
# print(res/b)
# print(sum(d.values())/len(d))

d = {'Math': 4, 'Ukrainian': 4, 'English': 5, 'Physic' : 5, 'Chemistry': 3}
marks = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
marks = {i:0 for i in range(1, 6)}

# print(max(d.values()))


#
# keys = [1, 2, 3, 4]
# values = [4, 5, 6]
# print(dict(zip(keys, values)))




