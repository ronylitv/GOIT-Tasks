new_list = []


def flatten(data):
    global new_list
    if len(data) == 0:
        return data
    else:
        for el in data:
            if isinstance(el, list):
                flatten(el)
                continue
            else:
                new_list.append(el)
        return new_list


l = [1, 2, [3, 4, [5, 6]], 7]
k = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
p = []
print(flatten(k))
