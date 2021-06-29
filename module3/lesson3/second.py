l = [0]
l *= 10
print(l)
# l[3] = 1
# l[4] = 1
# print(l)
l[3:5] = [2,2]
print(l)
s = 'adfgkkl'
s1 = s[:3] + 'aa' + s[5:]
print(s1)
s2 = s[:-1]
print(s2)


c =  (1, 2)
print(c[0])
print(c[1])
c = list(c)
c.append(3)
c = tuple(c)
print(c)


l1 = [1,2,3]
l2 = [1,2,3]
l3 = [1,2,3]
l = [l1, l2, l3]

print(len(l1), len(l2), len(l3))
for i in l:
    print(len(i), end = ' ')


answer = []
for i in l:
    answer += l

print(answer)
