def card_hide(card_number):
    card_number = card_number.replace(' ', '')
    if len(card_number) != 16:
        return 'Incorrect card number'
    else:
        counter = 0
        hidden_number = ''
        for i in card_number:
            counter += 1
            if i not in '1234567890':
                return 'Incorrect card number'
            elif counter <= 12:
                hidden_number += '*'
            else:
                hidden_number += i
        return hidden_number


print(card_hide("5556777899999090"))
