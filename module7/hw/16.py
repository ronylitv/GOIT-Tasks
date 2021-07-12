main_list = []


def decode(data):
    if len(data) == 0:
        return []
    else:
        f = [data[0] * data[1]]
        r = [i for i in f[0]]
        f = r + decode(data[2:])

        return f



print(decode(["X", 3, "Z", 2, "X", 6, "Y", 3, "Z", 2]))




# def decode(data):
#     if len(data) == 0:
#         return []
#     else:
#         f = data[0] * data[1] + str(decode(data[2:]))
#
#
#         return f
#
#
# print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))



