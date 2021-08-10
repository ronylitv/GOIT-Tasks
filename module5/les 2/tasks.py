import re


string = 'Нільс Бор народився в родині професора фізіології Копенгагенського університету Християна Бора (1858-1911) ' \
         'й Еллен Адлер (1860-1930). Батьки Бора одружилися 1881 року.' \
         'Батька Нільса Бора двічі висували кандидатом на Нобелівську премію з фізіології або медицини[6]. ' \
         'Мати була донькою впливового та вельми заможного єврейського банкіра і парламентаря-ліберала Давида/' \
         'Баруха Адлера[da] (1826-1878) і Дженні Рафаел (1830-1902) із британської єврейської банкірської династії Raphael ' \
         'Raphael & sons.'

# print(re.findall(r'[^0-9]', string))

# print(re.findall(r'^\w+', string))
# print(re.findall(r'(\w+)\.?$', string))
#
# pattern = r'[А-Яа-я]{3}\b'
# print(re.findall(pattern, string))


# pattern = r'\b\d{3}'
# print(re.findall(pattern, string))


# print(re.findall(r'\d{4}-\d{4}',string))
# print(re.findall(r'\d{4}-(\d{4})',string))
# print(re.findall(r'(\d{4})-\d{4}',string))
# print(re.findall(r'(\d{4})-(\d{4})',string))
#
# result_list = []
#
# iterator = re.finditer(r'(\d{4})-(\d{4})',string)
# for match in iterator:
#     result_list.append(match.group())
#
# print(result_list)
#

print(re.findall(r'@\w+\.(\w{les2,5})',string))
print(re.findall(r'https?:\/\/\w+\.?\w+',string))
