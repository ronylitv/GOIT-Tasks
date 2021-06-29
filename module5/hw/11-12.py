import re


def find_all_words(text, word):
    result = re.findall(word, text, re.IGNORECASE)

    return result


def replace_spam_words(text, spam_words):
    for i in spam_words:
        result = re.sub(i, '*' * len(i), text, 0, re.IGNORECASE)
        text = result
    return text
help(re.sub)

string = 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn ' \
         'language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn '
print(replace_spam_words(string, ['began', 'Python']))
