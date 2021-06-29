def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    phone_dict = {'UA': [],
                  'JP': [],
                  'TW': [],
                  'SG': []}
    for i in list_phones:
        sanitize_phone_number(i)
        if i.startswith('380'):
            phone_dict['UA'].append(i)
        elif i.startswith('81'):
            phone_dict['JP'].append(i)
        elif i.startswith('65'):
            phone_dict['SG'].append(i)
        elif i.startswith('886'):
            phone_dict['TW'].append
    return phone_dict
