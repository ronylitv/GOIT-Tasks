from collections import Counter
# def list_sum():
#     global l
#     print(l)
#     l += 3
#
# l = 3
# print(l)
# list_sum()
# print(l)

#
# def func(a, b = 5):
#     print(a, b)
# func(3, 4)
# func(3)

l = [1,2,3]
# def func():
#     global l
#     l.reverse()
# func()
# print(l)
# proytu

def str_count(s = ''):
    return dict(Counter(s))
s = 'hello'
print(str_count(s))

