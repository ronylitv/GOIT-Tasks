
def is_valid_pin_codes(pin_codes):
    data_set = set()
    val = True
    counter = 0
    for i in pin_codes:
        for j in i:
            if j in '1234567890':
                counter += 1
        if counter == 4:
            data_set.add(i)
            counter = 0
        else:
            val = False
    if len(data_set) != len(pin_codes) or len(pin_codes) == 0:
        val = False

    return val



print(is_valid_pin_codes([]))
