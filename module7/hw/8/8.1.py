import re
s = '2+ 34 - 5 * 3'
s = s.replace(' ', '')
wait_for_number = False
calculate = True
result_list = []

while calculate:
    if s[0] in '0123456789':
        wait_for_number = True

    while wait_for_number:
        try:
            res = re.search(r'\d+', s)
            result_list.append(res.group())
            s = s.replace(res.group(), '')
            wait_for_number = False
        except:
            calculate = False
    while not wait_for_number:
        try:
            result_list.append(s[0])
            s = s.replace(s[0], '')
            if s[0] not in '0123456789':
                result_list.append(s[0])
                wait_for_number = True
            else:
                wait_for_number = True
        except:
            calculate = False
            break

print(result_list)




