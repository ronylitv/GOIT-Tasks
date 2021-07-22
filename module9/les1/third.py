# def logged_func(func):
#     def inner(x, y):
#         print(f'called with {x}, {y}')
#         result = func(x, y)
#         print(f'result: {result}')
#         return result
#
#     return inner
#
#
# @logged_func
# def complicated(x, y):
#     return x / y

AGE = 15


def check(func):
    def inner():
        global AGE
        if AGE >= 18:
            func()
        else:
            print('Denied')
    return inner


@check
def hello_world():
    print('Hello, world')


hello_world()
