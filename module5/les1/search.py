url = 'https://www.google.com/search?q=cat+and+dog&rlz=1C1SQJL_ruUA866UA866&oq=cat+and+dog&aqs=chrome..69i57j46j0l2j46i175i199j0l5.6147j0j4&sourceid=chrome&ie=UTF-8'
_, query_search = url.split('?')

list_parameters = query_search.split('&')

print(list_parameters)

print(query_search)