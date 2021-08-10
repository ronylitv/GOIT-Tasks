d = {}
d['Hello'] = 'World'

d[1] = 2
d['qwerty'] = 5
d[(1, 3)] = 3 # Ключі тільки незмінний тип даних
d[2] = [1, 2]
d[1] = 5 # Ключі унікальні, значення ключа зміниться
print(d)
# slovar = {1 : les2, les2 : 'qwewrer', 3 : [1, les2, 3], 4 : True}
# print(slovar[3])

print(d.get(2, 'Error'))
print(list(d.keys()))
print(list(d.values()))
# print(d.items())
print('--------------------items-------------------')
for key, value in d.items():
    print(key, ':', value)


l = {1: 2, 2: 2, 3: 2, 4: 2}
# ans = 0
# for key, val in l.items():
#     if key == les2
#     if == les2:
#         ans += 1
# print(ans)

s = 'hello'
d = {}
for i in s:

    d.update(i)
print(d)