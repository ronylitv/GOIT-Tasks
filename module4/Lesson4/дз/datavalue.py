def lookup_key(data, value):
    items_list = []
    for ind, val in data.items():
        if val == value:
            items_list.append(ind)
    return items_list


def split_list(grade):
    first_list = []
    second_list = []
    try:
        average_number = sum(grade) / len(grade)

        for i in grade:
            if i <= average_number:
                first_list.append(i)
            else:
                second_list.append(i)
        return first_list, second_list
    except:
        return first_list, second_list

a = split_list([])
print(a)




