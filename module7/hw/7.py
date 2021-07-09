def data_preparation(list_data: list):
    new_list = []
    for el in list_data:
        if len(el) > 2:
            el.remove(max(el))
            el.remove(min(el))
        new_list.extend(el)
    new_list.sort()
    new_list.reverse()


    return new_list

print(data_preparation([[1,2,3],[3,4], [5,6]]))
print(data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]))
# data_list = [[1,2,3],[3,4], [5,6]]
# for el in data_list:
#     if len(el) > 2:
#         el.remove(max(el))
#         el.remove(min(el))
#
# print(data_list)