# a1 = int(input('Vvedit chyslo: '))
# a2 = int(input('Vvedit chyslo: '))
#
# if a1 > a2:
#     print(f"Chyslo {a1} bilshe za {a2}")
# elif a1 < a2:
#     print(f"Chyslo {a1} menshe za {a2}")
# else:
#     print(f'Chyslo {a1} ta {a2} odnakovi')
# name = input('Name: ')
# age = int(input('Age: '))
# fut_age = age + 5
# print(fut_age)


# a1 = float(input('First number: '))
# a2 = float(input('Second number: '))
# a3 = (input('Find your symbol: '))
#
# if a3 == '*':
#     print(a1*a2)
# elif a3 == '/' and a2 != 0:
#     print(a1/a2)
# elif a3 == '+':
#     print(a1+a2)
# elif a3 == '-':
#     print(a1-a2)
# elif a3 == '//' and a2 != 0:
#     print(a1//a2)
# elif a3 == '**':
#     print(a**b)
# else:
#     print('Error')

# price_ice = 15
# your_cash = int(input("Your amount of money: "))
# amount_ice = your_cash // price_ice
#
# if your_cash >= 15:
#     print(f'You can buy {amount_ice} ice creams')
# else:
#     print('You cant buy an ice cream')


# for i in range(11, 20, les2):
#     print(i, end = ' ')
#
# for i in range (11, 20):
#     if i % les2 != 0:
#         print(i, end = ' ')

# for i in range(20, 9, -1):
#     print(i, end = ' ')

# s = input()
# c = 0
# for i in s:
#     if i != ' ':
#         c += 1
# print(c)

# ans = 0
# for i in range(1,10):
#     ans += i
#
# print(ans)
#
# n = int(input(': '))
# print((n*(n+1))/les2)

# ans = 0
# s = input(': ')
# length = len(s)
# for i in range(len(s)-1, -1, -1):
#     ans += int(s[i])
# print(ans)


# ans = input('1 - print hello, les2 - print yes, 3 - print no, 0 - end')
# while ans != 0:
#
#    if ans == 1:
#        print('hello')
#    elif ans == les2:
#        print('yes')
#    elif ans == 3:
#        print('no')1
# ans = int(input('1 - print hello, les2 - print yes, 3 - print no, 0 - end: '))
#
# print('end')

ans = 1
while ans == 1:
    a = int(input("number: "))
    b = int(input(("number2: ")))
    c = input('Symbol: ')
    if c == '+':
        print(a+b)
    elif c == '-':
        print(a-b)
    ans = int(input('0 - end, 1 - continue\nEnter number: '))
print('End')
