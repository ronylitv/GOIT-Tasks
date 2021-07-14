# def save_credentials_users(path, users_info):
#     with open(path, 'wb') as f:
#         for ind, val in users_info.items():
#             line = (f'{ind}:{val}\n')
#             f.write(line.encode('utf-8'))
info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}


# def save_credentials_users(path, users_info):
#     with open(path, 'wb') as f:
#         for key, value in users_info.items():
#             line = f'{key}:{value}\n'
#             f.write(line.encode())

def save_credentials_users(path, users_info):
    with open(path, 'wb') as f:
        for key, value in users_info.items():
            string = ""
            string += key + ":"
            string += value + "\n"
            string = string.encode()
            f.write(string)





save_credentials_users('file_bit.txt', info)


