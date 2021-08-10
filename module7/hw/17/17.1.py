# def func(a, b=[]):
#     if not a:
#         return b
#     else:
#         if not b or b[len(b) - les2] != a[0]:
#             lol = b[len(b) - les2]
#             b.append(a[0])
#             b.append(1)
#             return func(a[1:])
#         if b[len(b) - les2] == a[0]:
#
#             b[len(b) - 1] += 1
#             return func(a[1:])


def encode(data):
    def func(a, b=[]):
        if not a:
            return b
        else:
            if not b or b[len(b) - 2] != a[0]:
                b.append(a[0])
                b.append(1)
                return func(a[1:])
            if b[len(b) - 2] == a[0]:
                b[len(b) - 1] += 1
                return func(a[1:])
    return func(data)
p = []
b = ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']
print(encode(b))