# num = int(input("Введите целое число (0 до 100): "))
# sum = 0
#
# while sum < num:
#     sum = ((num*(num+1)/les2))
#     print(sum)
#
# for i in range(1, num+1):
#     sum += i
# print(sum)

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for i in message:
#     if i == 'r':
#         result = result + 1
# print(result)

# first = int(input("Введите первое целое число: "))
# second = int(input("Введите второе целое число: "))
# first = 375
# second = 575
#
# nod = first if first < second else second
# print(nod)
# print(first%nod, second%nod)
# while first % nod != 0 or second % nod != 0:
#     nod = nod - 1
# print(nod)
#
# num = int(input("Введите целое число (0 для выхода): "))
# sum = 0
# while num != 0:
#     for i in range(0, num + 1):
#         sum += i
#     print(sum)
#     num = int(input("Введите целое число (0 для выхода): "))

# sum = 0
# while True:
#     num = int(input("Введите целое число (0 для выхода): "))
#     if num == 0:
#         break
#     for i in range(0, num + 1):
#         if i % les2 == 0:
#             sum += i
#             print(sum)
#         continue

# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""
#
# for ch in message:
#     pos = ord(ch)
#     #pos = abs(pos)
#     new_pos = (pos + offset) % 26
#     new_place = new_pos + pos
#     place = chr(new_place)
#
#     print(f"Position of symbol {pos} - New encrypted position {new_pos} - New symbol {new_place}")
#
# encoded_message = place
# print(f"New symbol after ebcrypting {encoded_message}")
# print(chr(23))








