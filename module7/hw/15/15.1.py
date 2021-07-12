
# def flatten(data):
#     if len(data) < 1:
#         return []
#     elif isinstance(data[0], list):
#         first_list = flatten(data[0])
#         second_list = flatten(data[1:])
#         main_list = first_list + second_list
#     elif not isinstance(data[0], list):
#         first_list = [data[0]]
#         second_list = flatten(data[1:])
#         main_list = first_list + second_list
#     return main_list

def flatten(data):
    if not data:
        return []
    if type(data[0]) == list:
        return flatten(data[0]) + flatten(data[1:])
    else:
        return [data[0]] + flatten(data[1:])

l = [1, 2, [3, 4, [5, 6]], 7]
k = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
p = []
print(flatten(p))

