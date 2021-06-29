phone_storage = ['380682450080', '0000000000',
                 '096 404 6372', '3805033 87099', '0503734441',
                 '380002450080', '+380682460080', '+38 (050) 33 870 99']

'''
+ 38 country code 050 code operator tel: 1234567
'''

codes_operator = {'039', '050', '063', '066', '068', '073', '091',
                  '096'}

def is_valid_phone(phone):

    if len(phone) == 12:
        if phone[:2] == '38':
            if phone[2:5] in codes_operator:
                return True
            else:
                return False

    if len(phone) == 10:
        if phone[:3] in codes_operator:
            return True
        else:
            return False
    return False

def _is_valid_phone(phone):
    def is_valid_operator(phone):
        if phone[:3] in codes_operator:
            return True
        return False

    if phone.isdigit():
        if len(phone) == 12:
            if phone[:2] == '38':
                return is_valid_operator(phone[2:])
        if len(phone) == 10:
            return is_valid_operator(phone)

        return False

def sanitize_number(phone):
    new_phone = (phone.strip()
                 # .removeprefix()
                 .replace('(', '')
                 .replace(')','')
                 .replace(' ','')
                 .replace('-', '')
                 .replace('+',''))
    return new_phone




def pretty_table():
    print('|{:^14}|{:^12}|'.format('Phone', 'Result'))
    print('|{:^14}|{:^12}|'.format('-' * 14, '-' * 12))
    for phone in phone_storage:
        phone = sanitize_number(phone)
        is_valid = is_valid_phone(phone)
        if is_valid:
            print('|{:^14}|{:^12}|'.format(phone, 'valid'))
        else:
            print('|{:^14}|{:^12}|'.format(phone, 'invalid'))

if __name__ == '__main__':
    pretty_table()


