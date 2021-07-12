# def get_employees_by_profession(path, profession):
#     names = ''
#     with open(path, 'r') as file:
#         lines = file.readlines()
#         for item in lines:
#             cleared_item = item.rstrip()
#             name_prof = cleared_item.split(' ')
#             if name_prof[1] == profession:
#                 names += name_prof[0]
#     return names
def get_employees_by_profession(path, profession):
    with open(path, 'r') as file:
        lines = file.readlines()
        for i in lines:
            index = i.find(profession)
            print(index)



print(get_employees_by_profession('prof.txt', 'cook'))
