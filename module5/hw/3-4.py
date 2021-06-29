def sanitize_phone_number(phone):
    phone = (phone.strip()
             .replace(' ', '')
             .replace('(', '')
             .replace(')', '')
             .replace('-', '')
             .removeprefix('+'))

    return phone


a = sanitize_phone_number('+380(68)2450080')
print(a)


def get_phone_numbers_for_countries(list_phones):
    phone_dict = {'JP': [],
                  'SG': [],
                  'TW': [],
                  'UA': []}
    for i in list_phones:
        sanitized_number = sanitize_phone_number(i)
        print(sanitized_number)
        if sanitized_number.startswith('380'):
            phone_dict['UA'].append(sanitized_number)
        elif sanitized_number.startswith('81'):
            phone_dict['JP'].append(sanitized_number)
        elif sanitized_number.startswith('65'):
            phone_dict['SG'].append(sanitized_number)
        elif sanitized_number.startswith('886'):
            phone_dict['TW'].append(sanitized_number)
    return phone_dict


print(get_phone_numbers_for_countries(['+380(682)450080', '+380964046372']))

# def is_check_name(fullname, first_name):
#     return True if fullname.startswith(first_name) else False
