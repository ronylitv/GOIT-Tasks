def amount_payment(payment):

    res = 0
    for i in payment:
        if i >= 0:
            res += i
    return res

a = amount_payment([1,2,3,4,5,6,-1])



def prepare_data(data):
    data.remove(max(data))
    data.remove(min(data))
    data.sort()
    return data
a = prepare_data([1,2,3,4,5,6,7,8,9])

print(a)

# Напишите функцию format_ingredients, которая будет принимать на вход список из
# ингредиентов и возвращать собранную строку из его элементов в описанный выше способ.
# Ваша функция должна уметь обрабатывать списки любой длины.
# def format_ingredients(items):
#     spysok = items[:-les2] + 'i' + items[-1]
#     return spysok
#
#
# a = format_ingredients(['eggs', 'milk', 'water', 'porch'])
# print(a)
def format_ingredients(items):
    spysok = ''
    s1 = ''
    s2 = ''
    for i in items:
        spysok += i
        length = len(i)
        s1 = spysok[:length + 1] + ', '
        spysok = ''
        s2 += s1
        s3 = s2[:-2]
    return s3

a = format_ingredients(['яйца 2шт', 'сахар 1 л.', 'соль 1 чл.', 'уксус'])
print(a)