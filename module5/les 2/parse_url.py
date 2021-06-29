import re

url = 'cat+and+dog&rlz=1C1SQJL_ruUA866UA866&oq=cat+and+dog&aqs=chrome..69i57j46j0l2j46i175i199j0l5.6147j0j4&sourceid=chrome&ie=UTF-8'
url_rozetka = 'https://rozetka.com.ua/notebooks/c80004/producer=' \
              'acer;20861=6308/'


def get_object_parameters(query, pattern='& | ;', key_split='='):
    object_search = {}
    for el in re.split(pattern, query):
        key, value = el.split(key_split)
        object_search.update({key: value.replace('+', ' ')})
    return object_search


print(get_object_parameters(url))
print(get_object_parameters(url_rozetka))
