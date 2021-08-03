# def read_employees_from_file(path):
#     fh = open(path, 'r')
#     list_of_salaries = fh.readlines()
#     new_list = []
#     for i in list_of_salaries:
#         b = i.replace('\n', '')
#         new_list.append(b)
#     fh.close()
#     return new_list



# def read_employees_from_file(path):
#
#     list1 = []
#     fh = open(path, 'r')
#     list = fh.readlines()
#     for i in list:
#             list1.append(i.strip())
#     fh.close()
#
#     return list1
def read_employees_from_file(path):
    f_employees = open(path, 'r')
    l_employees = []
    for i in f_employees.readlines():
        i = i.strip()
        l_employees.append(j)
    f_employees.close()
    return l_employees
print(read_employees_from_file('salary1.txt'))

