# url_rozetka = 'https://rozetka.com.ua/notebooks/c80004/producer=' \
#               'acer;20861=6308/'
#
# query_url_rozetka = 'producer=acer;20861=6308'
#
# query_rozetka = query_url_rozetka.split(';')
# print(query_rozetka)
url = 'https://www.google.com/search?q=cat+and+dog&rlz=1C1SQJL_ruUA866UA866&oq=cat+and+dog&aqs=chrome..69i57j46j0l2j46i175i199j0l5.6147j0j4&sourceid=chrome&ie=UTF-8'
_, query_search = url.split('?')

list_parameters = query_search.split('&')

print(list_parameters)

print(query_search)

object_search = {}
for el in list_parameters:
    key, value = el.split('=')
    object_search.update({key:value})

print(object_search)
url_str = ''
for key, value in object_search.items():
    url_str = url_str + '='.join([key, value.replace(' ','+')])
print(url_str)





