import re


# def total_salary(path) -> float:
#     fh = open(path, 'r')
#     new_list = []
#     while True:
#         line = fh.readline()
#         res = line.split(',')
#         new_list.append(res)
#         if not line:
#             break
#     return new_list
#
#
# print(total_salary('salary.txt'))

def total_salary(path):
    fh = open(path, 'r')
    salaries = []
    while True:
        line = fh.readline()
        result = re.search(r'\d+', line)
        try:
            salaries.append(int(result.group()))
        except:
            pass
        if not line:
            break
    fh.close()

    return float(sum(salaries))


print(total_salary('salary.txt'))
