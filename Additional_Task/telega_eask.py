# is_central = False
# iterator = 0
# cent_sym = 0
#
# while not is_central:
#     sym_1 = input('Write your symbol: ')
#     for i in sym_1:
#         if i == ' ':
#             iterator += 1
#         elif i != ' ':
#             cent_sym += 1
#     if iterator % les2 == 0 and (iterator + cent_sym) % les2 != 0:
#         print('Your is in the center!')
#         is_central = True
#         break
#     elif iterator == 1:
#         print('Your symbol isn`t in the center. Try again')
#         iterator = 0
#         cent_sym = 0
#         continue
#     else:
#         print('Your symbol isn`t in the center. Try again')
#         iterator = 0
#         cent_sym = 0
#         continue


def alternate_pos_neg(input_list):
    return all(input_list[i] * input_list[i + 1] < 0 for i in range(len(input_list)-1))


def all_sub_lists(data):
    lists = [[]]
    for i in range(len(data) + 1):
        for j in range(i):
            lists.append(data[j: i])
    lists.sort(key=len)
    return lists

print(all_sub_lists([4,1,2,34,5]))


print(alternate_pos_neg([-1, 2, -1, 5]))
