def formatted_numbers():
    num_list = []
    begin = '|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary')
    num_list.append(begin)
    for i in range(0, 16):
        s = '|{0:^10d}|{0:^10x}|{0:^10b}|'.format(i)
        num_list.append(s)
    return num_list

for i in formatted_numbers():
    print(i)