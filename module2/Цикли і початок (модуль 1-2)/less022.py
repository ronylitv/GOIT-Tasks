# n = int(input(':   '))
# n = abs(n)
# ans = 0
# while n:
#     ans += n // 10
#     n %= 10
# print(ans)

# n = int(input(':   '))
# n = abs(n)
# ans = 0
# while n:
#     ans = ans * 10 + n % 10
#     n //= 10
# print(ans)
n = 2
while True:
    print(n)
    n -= 1
    if n == 1:
        break

# login = 'Admin'
# password = 'root'
# ans = 1
# while ans:
#     log = input('Login: ')
#     pas = input("pass: ")
#     if login == log or password == pas:
#         print('welcome')
#         ans = 0
#     else:
#         print('Tryafain')
#         ans = int(input("Do u eant to try again?: "))
# for i in range(len(s)):
#     if s[i] == 'a':
#         c = 1
#         print(i)
#         break

# sum = 0
# print(sum)
# for i in s:
#     if i in 'aAoOiIeEuUyY':
#         sum += 1
# print(sum)
res = int(1)
b = int(input(': '))
# for i in range(1, b + 1):
#     res *= i
#     i = i - 1
#     if b == 0:
#         res = 1
# print(res)

while True:
    res *= b
    b = b - 1
    if b == 0:
        break
print(res)