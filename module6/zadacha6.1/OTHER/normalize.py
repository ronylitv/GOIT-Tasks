import re

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
LAT_TRANS = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
             "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}

for key, value in zip(CYRILLIC_SYMBOLS, LAT_TRANS):
    TRANS[ord(key)] = value
    TRANS[ord(key.upper())] = value.upper()


def normalize(string) -> str:
    translated_string = string.translate(TRANS)
    translated_string = re.sub(r'\W', '_', translated_string)
    return translated_string


 # for i in translated_string:
    #     if i not in TRANS.values() and not i.isdigit():
    #         new_str += '_'
    #     else:
    #         new_str += i
    #
    # return new_str

