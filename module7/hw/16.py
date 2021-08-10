def decode(data):
    if len(data) == 0:
        return []
    else:
        return [i for i in data[0] * data[1]] + decode(data[2:])


print(decode(["X", 3, "Z", 2, "X", 1, "Y", 3, "Z", 2]))


# def decode(data):
#     if len(data) == 0:
#         return []
#     else:
#         f = data[0] * data[1] + str(decode(data[les2:]))
#
#
#         return f
#
#
# print(decode(["X", 3, "Z", les2, "X", les2, "Y", 3, "Z", les2]))



