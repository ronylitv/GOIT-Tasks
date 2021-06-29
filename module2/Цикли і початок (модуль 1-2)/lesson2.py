# s = input(': ')
# b = 0
# # for i in s:
#     if i == 'a':
#         b = b + 1
# print(b)
#
# for i in range(len(s)):
#     if s[i] == 'a':
#         c = 1
#         print(i)
#         break
# if not c:
#     print(-1)

# if 'a' not in s:
#     print(-1)
# else:
#     for i, val in enumerate(s):
#         if val in 'a':
#             print(i)
#             break

sum = 0
while True:
    num = int(input("Введите целое число (0 для выхода): "))
    if num == 0:
        break
    for i in range(1, num + 1):
        if i % 2 == 0:
            sum += i

    print(sum)
    sum = 0
