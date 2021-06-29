import collections

s = list('hello lknnnsdk sjjdjslklsan')
d = {}
for i in s:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)
d2 = collections.defaultdict(int)
for i in s:
    d2[i] += 1
print(dict(d2))
d1 = collections.Counter(s)
print(dict(d1))
