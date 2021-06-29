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
#     if iterator % 2 == 0 and (iterator + cent_sym) % 2 != 0:
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
