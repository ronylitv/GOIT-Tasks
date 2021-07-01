from pathlib import Path

message = 'Привет мир!'

print(message.encode())
print(message.encode('utf_16'))
print(message.encode('utf_16'))
print(message.encode('cp1251'))

print(b'\xcf\xf0\xe8\xe2\xe5\xf2 \xec\xe8\xf0!'.decode('cp1251'))

folder = Path('Test')
with open(folder / 'utf-8.txt', 'wb') as f:
    f.write(message.encode('utf-8'))
with open(folder / 'utf-16.txt','wb') as f:
    f.write(message.encode('utf-16'))
with open(folder / 'cp1251.txt', 'wb') as f:
    f.write(message.encode('cp1251'))