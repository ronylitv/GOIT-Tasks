variable = 'Hello'

def calc(a, b, c):
    if c == '+':
        res = a + b
        return res
    elif c == '-':
        res = a - b
        return res
    elif c == '*':
        res = a * b
        return res
    elif c == '/':
        res = a / b
        return res


def func():
    print(f'Hello World')
