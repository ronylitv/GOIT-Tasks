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


# def get_cats_info(path):
#     cats_info = []
#     with open(path, 'r') as fh:
#         lines = fh.readlines()
#         for i in lines:
#             id_data, name_data, age_data = i.split(',')
#             cats = dict(id='', name='', age='')
#             cats['id'] = id_data
#             cats['name'] = name_data
#             cats['age'] = age_data.strip()
#             cats_info.append(cats)
#
#     return cats_info

def get_cats_info(path):
    result = []
    with open(path, "r") as f:
        for string in f.readlines():
            id, name, age = string.split(",")
            result.append({"id": id, "name": name, "age": age.strip()})
    return result


# def get_cats_info(path):
#     id = ''
#     name = ''
#     age = ''
#     result = [{'id': id}, {'name': name}, {'age': age}]
#     with open(path, 'r') as fh:
#         strings = fh.readline()
#         strings1 = strings.split(",")
#         for i in strings1:
#             if len(i) == 24:
#                 id += i
#             if len(i) > 2 and len(i) < 8:
#                 name += i
#             if len(i) > 1 and len(i) < 3:
#                 i = i.replace("\n", "")
#                 age += i
#     return result

print(get_cats_info('cats.txt'))
