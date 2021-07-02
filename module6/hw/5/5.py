# def get_cats_info(path):
#     def sanitize_age(age):
#         return age.strip()
#
#     cats_info = []
#     with (open(path, 'r')) as fh:
#         while True:
#             line = fh.readline()
#             data_values = line.split(',')
#             cats = dict(id='', name='', age='')
#             try:
#                 cats['id'] = data_values[0]
#                 cats['name'] = data_values[1]
#                 cats['age'] = sanitize_age(data_values[2])
#             except:
#                 break
#             cats_info.append(cats)
#
#             if not line:
#                 break
#     return cats_info
#
#
# print(get_cats_info('cats.txt'))

# text = '60b90c1c13067a15887e1ae1,Tayson,3\n'
# sent = text.split(',')
# print(sent)


def get_cats_info(path):
    cats_info = []
    with open(path, 'r') as fh:
        lines = fh.readlines()
        for i in lines:
            id_data, name_data, age_data = i.split(',')
            cats = dict(id='', name='', age='')
            cats['id'] = id_data
            cats['name'] = name_data
            cats['age'] = age_data.strip()
            cats_info.append(cats)

    return cats_info

print(get_cats_info('cats.txt'))
