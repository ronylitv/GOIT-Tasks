import re

s = "I am 25 years old"
age = re.search('\d+', s)


def find_word(text, word):
    result = re.search(word, text)
    if result:
        new_dict = {
            'result': True,
            'first_index': result.span()[0],
            'last_index': result.span()[1],
            'search_string': word,
            'string': text

        }
    else:
        new_dict = {
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': word,
            'string': text

        }
    return new_dict

print(find_word("Guido van Rossum "
                "began working on Python in "
                "the late 1980s, as a successor"
                " to the ABC programming language, and first released it in 1991 as Python 0.9.0.", "Python"))
