def calc(a, b, sign):
    if sign == '+':
        res = a + b
        return res
    elif sign == '-':
        res = a - b
        return res
    elif sign == '*':
        res = a * b
        return res
    elif sign == '/':
        res = a / b
        return res
    else:
        return 'ERror'