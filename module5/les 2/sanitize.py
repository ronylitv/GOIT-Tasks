import re

string = 'Say hi i love [stroka grupy] lambda ya lubly [tebe]'

lang = 'The best language Java'
pattern = 'Java'

result = re.sub(pattern, 'Python', lang)

print(result)

pattern = r'\[.*?\]'
result = re.sub(pattern, '', string)
print(result)
