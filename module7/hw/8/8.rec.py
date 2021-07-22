import re


def token_parser(s):
    s = s.strip()
    b = []
    if len(s) < 1:
        return []
    for i in s:
        if i in '0123456789':
            res = re.search(r'\d+', s)
            b.append(res.group())
            return b + token_parser(s[len(res.group()):])
        else:
            b.append(i)
            return b + token_parser(s[1:])


print(token_parser('31232+32313-632347-233343*(21233+43321)'))
print(token_parser('2+34-5*3'))

