def summ(a, b):
    return a + b
def minus(a, b):
    return a - b
def dil(a, b):
    return a / b
def mnozh(a, b):
    return a * b

def calc(a, b, c):
    if c == "+":
        return summ(a,b)
    elif c == '-':
        return minus(a, b)
    elif c == '/':
        return dil(a, b)
    elif c == '*':
        return mnozh(a, b)

p = calc(4, 5, '*')
print(p)