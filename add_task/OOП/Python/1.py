def fact(n, acc=1):
    if n == 0:
        return acc
    return fact(n-1, acc * n)