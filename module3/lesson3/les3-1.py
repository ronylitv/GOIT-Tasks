
# sort - сортировка
# pop - видалити по індексу
# remove - видалити по значенню
# append - dodaty
# extend - добавити в список
# insert - вставляємо на (місце, аргумент)
l = []
for i in range(1, 11):
    if i % 2 == 0:
        l.append(i)

print(l)

l = [i for i in range(2, 11, 2)]
print(l)
l2 = [i if not i%2 else 0 for i in range(1, 11)]
print(l2)
l3 = [0 if i%2  else 1 for i in range(10)]
print(l3)

l3 = [1 if i%2 != 0 else 0 for i in range(10)]
print(l3)

l4 = [i for i in range(10, 0, -1)]
print(l4)

s = 'Hello World!'
l5 = [i for i in s if i not in 'aeoyuiAEOYUI']
print(l5)
l7 = [i for i in s if i in ['a', 'e', 'o', 'y', 'u', 'i']]
l6 = [i for i in s if i in 'a e o y u i A E O Y U I'.split(' ')]
print(l6)