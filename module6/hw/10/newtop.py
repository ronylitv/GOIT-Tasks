def get_credentials_users(path):
    with open(path, 'rb') as f:
        lines = f.readlines()
        pos = 0
        for el in lines:
            lines[pos] = el.decode()
            pos += 1
        lop = [i.strip() for i in lines]

    return lop



print(get_credentials_users('file_bit.txt'))
