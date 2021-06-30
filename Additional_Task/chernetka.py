# def real_len(text):
#     new_list = ['\n', '\f', '\r', '\t', '\v']
#     count = 0
#     for i in text:
#         if i in new_list:
#             count += 1
#     return len(text) - count
#
# text = 'Hello\nWorld\v'
# print(len(text))
# print(real_len(text))
#

from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_num = False
    for ch in password:
        if ch >= "A" and ch <= "Z":
            has_upper = True
        elif ch >= "a" and ch <= "z":
            has_lower = True
        elif ch >= "0" and ch <= "9":
            has_num = True
    if len(password) == 8 and has_upper and has_lower and has_num:
        return True
    return False


def get_password():

    while True:
        rand_pass = get_random_password()
        if is_valid_password(rand_pass):
            return rand_pass
        else:
            continue

print(get_password())








