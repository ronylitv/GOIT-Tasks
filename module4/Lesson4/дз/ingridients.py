def format_ingredients(items=''):
    new_list = ''
    if len(items) == 1:
        for i in items:
            new_list = i
        return new_list
    elif len(items) > 1:
        last_item = items[-1]
        s1 = items[:-1]
        for i in s1:
            new_list += i + ', '
        new_list = new_list[:-2] + ' и ' + last_item

        return new_list
    else:
        return ''


a = format_ingredients([])
print(a)
