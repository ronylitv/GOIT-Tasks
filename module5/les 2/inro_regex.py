import re

string = 'Нільс Бор народився в родині професора фізіології Копенгагенського університету Християна Бора (1858—1911) ' \
         'й Еллен Адлер (1860—1930). Батьки Бора одружилися 1881 року.' \
         'Батька Нільса Бора двічі висували кандидатом на Нобелівську премію з фізіології або медицини[6]. ' \
         'Мати була донькою впливового та вельми заможного єврейського банкіра і парламентаря-ліберала Давида/' \
         'Баруха Адлера[da] (1826—1878) і Дженні Рафаел (1830—1902) із британської єврейської банкірської династії Raphael ' \
         'Raphael & sons '

pattern = r'\d+'
result = re.search(pattern, string)
# print(result.span())
# print(result.group())
# print(result.string)

pattern = r'\d'
result = re.findall(pattern, string)

print(result)
print(len(result))

result = re.findall(r'[0-9]{4}', string)
result = re.findall(r'\d{4}', string)
result = re.findall(r'[А-Я]', string)
pattern = r'\d'
new_pattern = re.compile(pattern)

result = new_pattern.findall(string)

print(len(result))
