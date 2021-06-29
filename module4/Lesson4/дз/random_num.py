from random import randint

def get_random_password():
    random_pass = ''
    for i in range(1, 9):
        random_num = randint(40, 126)
        random_num = chr(random_num)
        random_pass += random_num

    return random_pass

print(get_random_password())



