def save_credentials_users(path, users_info):
    with open(path, 'wb') as f:
        for ind, val in users_info.items():
            line = (f'{ind}:{val}\n')
            f.write(line.encode('utf-8'))
info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
save_credentials_users('file_bit.txt', info)
