# def read_employees_from_file(path):
#     fh = open(path, 'r')
#     list_of_salaries = fh.readlines()
#     new_list = []
#     for i in list_of_salaries:
#         b = i.replace('\n', '')
#         new_list.append(b)
#     fh.close()
#     return new_list



def read_employees_from_file(path):

    list1 = []
    fh = open(path, 'r')
    list = fh.readlines()
    for i in list:
            i = i.replace("\n", "")
            list1.append(i)
    fh.close()

    return list1

print(read_employees_from_file('salary1.txt'))
# aaa = [{'1': 2, '2': 3, '3': 4}, {'1a': 2, '2a': 3, '3a': 4}, {'1b': 2, '2b': 3, '3b': 4}]
# b = []
# key = '1'
#
# for i in aaa:
#     for j in i:
#         if key == j:
#             b.append(j)
# print(b)
