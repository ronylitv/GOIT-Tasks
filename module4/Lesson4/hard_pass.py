def is_valid_password(password):
    number = False
    high_symbol = False
    lower_symbol = False

    for i in password:
        if i in '1234567890':
            number = True
        elif i == i.upper() and i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            high_symbol = True
        elif i == i.lower() and i in 'qwertyuiopasdfghjklzxcvbnm':
            lower_symbol = True
    if number and high_symbol and lower_symbol and len(password) == 8:
        return True
    return False

print(is_valid_password('123Fa111'))















