import re
from typing import List, Any

def token_parser(s):
    numbers = re.findall(r'\d+', s)
    operators: list[Any] = re.findall(r'[-,+,*,/,(,)]', s)
    leks_list = []
    pos=0
    while True:
        if s[0] in '0123456789':
            try:
                leks_list.append(numbers[pos])
                leks_list.append(operators[pos])
                pos += 1
            except:
                break
        else:
            try:
                leks_list.append(operators[pos])
                leks_list.append(numbers[pos])

                pos += 1
            except:
                break


    return leks_list

# def token_parser(s):
#     s = s.replace(' ', '')
#     count = 0
#     while True:
#         try:
#             res = re.search(r'\d+', s)
#             count += 1
#             if count > 5:
#                 break
#         except:
#             break
s = '2+ 34 - 5 * 3'
s = s.replace(' ', '')
digit_positions = []
while True:
    try:
        res = re.search(r'\d+', s)
        pos_dict = {
            'start_pos': res.span()[0],
            'last_pos': res.span()[1],
            'value': res.group()
        }
        digit_positions.append(pos_dict)
        s.replace(res.group(), '')
    except:
        break



# print(token_parser('2+ 34 - 5 * 3'))
# print(token_parser('(2+ 3) *4 - 5 * 3'))
