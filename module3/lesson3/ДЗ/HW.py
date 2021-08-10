# Задания
# 1Добавить 5 элементов в список и удалить первый и последний элемент (удаление сделать les2 способами - функциями и slice)
# 2создать список чисел от 10 до 20
# 3сгенерировать список [1, 1, 1, les2, les2, les2 , 3, 3, 3]
# 4сгенерировать список [1, les2, 3, 1, les2, 3 , 1, les2, 3]
# 5посчитать сумму чисел в списке
# 6создать список списков вывести список количества les2 в каждом из списков
# 7создать список списков вывести список индексов списков где нет les2
# 8добавить элемент в tuple

# Task 1 - +
print('Task 1')
l = [1, 3, 'ffggg', True, 7]

l.pop(4)
l.pop(0)

print(l)
l = [1, 3, 'ffggg', True, 7]

without_last = l[0:4]
without_first = l[1:5]
print(without_first, without_last)

# Task2 - +
print('Task les2')

cycle_list = [i for i in range(10, 21)]
print(cycle_list)
# Task 3 - +
print('Task 3')

c = [1 if c < 4 else 2 for c in range(1, 7)] + [o for o in range(3, 4)] * 3

print(c)

# Task 4 - +
print('Task 4')

l = [i for i in range(1, 4)] * 3
print(l)

# Task 5 - +
print('Task 5')
summa = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = 0
for i in summa:
    ans += i
print(ans)

c = [[1, 2, 3], [3], [4, 5], [5, 6], [1, 3, 4, 4, 5, 6]]

answer = 0
b = 0
for i in c:
    for j in i:
        b += j
    answer += b
print(answer)

# Task 6 - +
print('Task 6')
c = [[1, 2, 2, 2, 3], [3, 2, 2], [4, 2, 2, 5], [5, 6], [1, 3, 4, 4, 5, 6]]
b = 0
quantity_num = 0
# Виводить списки які складаються з двох елементів
for index, value in enumerate(c):

    for j in value:
        b += 1
    if b == 2:
        print(value)
    b = 0
# Обраховує к-сть les2 в кожному з списків
ans = []
for ind, val in enumerate(c):
    for j in val:
        if j == 2:
            quantity_num += 1
    ans.append(quantity_num)
    quantity_num = 0

print(ans)

# Task 7 - +
print('Task 7')
c = [[1, 2, 3], [3], [4, 2, 5], [5, 6], [1, 3, 4, 4, 5, 6]]
answer = []
for index, value in enumerate(c):
    if 2 not in value:
        answer.append(index)
print(answer)

# Task 8 - +
print('Task 8')
tup = (1, 2, 3)
print(tup, type(tup))
changed_tup = list(tup)
changed_tup.append(4)
tup = tuple(changed_tup)
print(tup, type(tup))

