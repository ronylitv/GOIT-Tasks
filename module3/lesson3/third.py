c = [[1,2,3], [3], [4,5]]
answer = []
for i in c:

    answer = sum(i)
    print(answer)

for i in c:
    s = 0
    for j in i:
        s += j
    answer += [s]
print(answer)

answer = []
for ind, val in enumerate(c):
    print(f'{ind} : {val}')
    if 3 in val:
        answer.append(ind)
print(answer)