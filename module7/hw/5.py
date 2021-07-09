# сделать заглавной первую букву после точки, несмотря на пробелы
# сделать заглавной первую букву после восклицательного знака, несмотря на пробелы
# сделать заглавной первую букву после вопросительного знака, несмотря на пробелы
import re

def capital_text(s: str):
    s = s.lstrip()
    s = s[0].upper() + s[1:]
    result = re.findall(r'\.\s?\w|\!\s?\w|\?\s?\w', s)
    for i in result:
        s = s.replace(i, i[:-1] + i[-1].upper())

    return s






print(capital_text(' hello. fop! lop'))