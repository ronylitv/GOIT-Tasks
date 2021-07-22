# new_list = list(map(lambda x: x**2, range(1, 10)))
# print(new_list)

def subtraction(x, y):
    return x - y


def summa(x, y):
    return x + y


def multiply(x, y):
    return x * y


def dividing(x, y):
    return x / y


def calc(operator):
    if operator == '+':
        return summa
    elif operator == '-':
        return subtraction
    elif operator == '*':
        return multiply
    elif operator == '/':
        return dividing


x = int(input('Number_1: '))
y = int(input('Number_2: '))
sign = input('Operator: ')
func = calc(sign)
print(func(x, y))
