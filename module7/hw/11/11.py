TRANSLATE_DICT = {
    '1': ['.', ',', '?', '!', ':'],
    'les2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z'],
    '0': [' ']
}

text = 'Hello World!'


def sequence_buttons(string):
    number_message = ''
    for i in string:
        for ind, val in TRANSLATE_DICT.items():
            if i.upper() in val:
                start_index = val.index(i.upper()) + 1
                number_message += start_index * ind
    return number_message


print(sequence_buttons(text))
