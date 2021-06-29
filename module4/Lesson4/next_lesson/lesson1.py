RADIUS: float = 637.9021
# -> float очікує повертати тип флоат
count = 0


#
#
# def foo():
#     global count
#     count += 1
#
#
# def baz():
#     global count
#     count += 1
#
# baz()
# foo()
# print(count)
def first(size, *args):
    print(list(args))
    return size, args

print(first(5, 4,5,'hi'))
def second(size, **kwargs):
    print(list(kwargs))
    return size, len(kwargs),  kwargs

print(second(5, a = 4, b = 5))


def modeling(factor, *_, correction=1):
    return factor * correction

def third(size, *args,  **kwargs):
    print(list(args))
    print(kwargs)

    return size, len(kwargs), len(args),  kwargs

print(third(5, 4, 5, 'hi', ))

