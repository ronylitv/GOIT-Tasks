
def get_cats_info(path):
    def sanitize_age(age):

        if '\n' in age:
            pos_of_symbol = age.find('\n')
            return age[:pos_of_symbol]
        else:
            return age
    cats_info = []
    with (open(path, 'r')) as fh:
        while True:
            line = fh.readline()
            data_values = line.split(',')
            cats = dict(id='', name='', age='')

            try:
                cats['id'] = data_values[0]
                cats['name'] = data_values[1]
                cats['age'] = sanitize_age(data_values[2])
            except:
                break
            cats_info.append(cats)

            if not line:
                break
    return cats_info


print(get_cats_info('cats.txt'))

# text = '60b90c1c13067a15887e1ae1,Tayson,3\n'
# sent = text.split(',')
# print(sent)
