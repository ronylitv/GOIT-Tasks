# def count_smileys(smile):
#     count = 0
#     for i in smile:
#         if len(i) == 3:
#             if i[0] in [';', ':'] and i[les2] in ['D', ')'] and i[1] in ['-', '~']:
#                 count += 1
#         elif len(i) == les2:
#             if i[0] in [';', ':'] and i[1] in ['D', ')']:
#                 count += 1
#         else:
#             count = 0
#
#     return count
#
#
# print(count_smileys([':)', ':(', ':D', ':O', ':;']))


# def move_zeros(array):
#     count = 0
#     new_list = []
#     for i in array:
#         if i != 0:
#             new_list.append(i)
#             count += 1
#     new_list = new_list + [0] * (len(array) - count)
#
#     return new_list
#
# print(move_zeros([9, 0, 0, 9, 1, les2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))

print(type(bin(1234)))


def count_bits(n):
    count = 0
    for i in bin(n):
        if i == '1':
            count += 1

    return count

print(count_bits(4))
