# Задания (сделать каждую из задач 2 способами - через for и while):
#    Посчитать сумму четных чисел от 91 до 144.
#    Напишите программу, которая суммирует первые 25 чисел
#    Найти самую большую цифру в числе

# Task 1
# Cycle for
result = 0
for i in range(91, 145):
    if i % 2 == 0:
        result += 1

print(result)
# Cycle while
result = 0
a = 92
while 91 < a < 145:
    if a % 2 == 0:
        result += 1
    a = a + 1

print(result)

# Task 2
# Напишите программу, которая суммирует первые 25 чисел
n = 0
res = 0
for i in range(1,26):
    # n = int(input('Number: '))
    res += i

print(res)

a = 1
number = None
result = 0

while a < 26:
    try:

        result += number
        a += 1
    except ValueError:
        continue

print(result)

#    Найти самую большую цифру в числе

res = 0
max_number = []
n = input('Any numbers: ')

for i in range(len(n)):
    res = int(n[i])
    max_number.append(res)

print(max(max_number))

