# Задания:
# 1 Создать словарь, где ключи и значения числа
# 2 Посчитать сумму ключей, значений, всех абсолютно чисел
# 3 Вывести значения, где ключи - четные числа
# 4 Вывести самый большой ключ
# 5 Вывести значение пары с самым маленьким ключем
# 6 Удалить пару где ключ 3
# 7 Сгенерировать словарь:
# {1:5, 2:4, 3:3, 4:2, 5:1}
# {1:5, 2:4, 3:0, 4:2, 5:1}
# 8 Найти среднее значение всех ключей
# 9 Попробовать все методы множеств

# Task 1 - +
slovar = {1: 190, 2: 2, 3: 3, 4: 5, 5: 7}
print('\n---------Task 2------------\n')
# Task 2 - +
p = (sum(slovar.keys()))
b = (sum(slovar.values()))
a = p + b
print(f'Сума ключів: {p}\nСума значень: {b}\nСума всіх абсолютно чисел: {a}')
print('\n---------Task 3------------\n')
# Task 3 - +

for i in slovar.keys():
    if i % 2 == 0:
        b = slovar[i]
        print(f'The values of odd keys in dict: {b}')
print('\n---------Task 4------------\n')
# Task 4 - +

print(max(slovar.keys()))
print('\n---------Task 5------------\n')

# Task 5 - +

print(slovar[min(slovar.keys())])
print('\n---------Task 6------------\n')
# Task 6 - +

slovar.pop(3)
print(slovar)
print('\n---------Task 7------------\n')

# Task 7 -
# {1:5, 2:4, 3:3, 4:2, 5:1} +
# {1:5, 2:4, 3:0, 4:2, 5:1} +
d = {ind: val for ind, val in enumerate (range(6, 0, -1)) if ind >= 1}
d1 = {ind: val for ind, val in enumerate (range(6, 0, -1)) if ind >= 1}
d1[3] = 0
print(d, d1)
print('\n---------Task 8------------\n')
#Task 8 - +

a = (sum(slovar.keys()))/len(slovar)
print(f'The avarage number of keys: {a}')
print('\n---------Task 9------------\n')
# Task 9 -
but = {1, 2, 3, 4, 5, 6, 6, 5}
print(but, type(but))
but.add('hello')
print(but, type(but))
but.remove('hello')
but.discard(3)
print(but, type(but))