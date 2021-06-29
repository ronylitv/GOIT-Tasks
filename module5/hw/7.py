CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
LAT_TRANS = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
             "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}

for key, value in zip(CYRILLIC_SYMBOLS, LAT_TRANS):
    TRANS[ord(key)] = value
    TRANS[ord(key.upper())] = value.upper()


def normalize(string):
    translated_string = string.translate(TRANS)
    return translated_string



