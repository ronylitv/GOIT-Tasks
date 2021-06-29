# s = 'hello'
# for i, val in enumerate(s):
#     print(f"{i}:{val}")

b = '11232132'
res = int()
for i in range(len(b)):
    res += int(b[i])
print(res)

n = int(input(':   '))
n = abs(n)
ans = 0
while n:
    ans += n % 10
    n //= 10
print(ans)
