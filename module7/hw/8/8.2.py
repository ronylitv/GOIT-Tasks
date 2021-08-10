import re


def token_parser(s):
    s = s.replace(' ', '')
    wait_for_number = False
    calculate = True
    result_list = []

    while calculate:
        try:
            if s[0] in '0123456789':
                wait_for_number = True
        except IndexError:
            break

        while wait_for_number:
            try:
                res = re.search(r'\d+', s)
                result_list.append(res.group())
                s = s.replace(res.group(), '', 1)
                wait_for_number = False
            except IndexError:
                calculate = False
        while not wait_for_number:
            try:
                result_list.append(s[0])
                s = s.replace(s[0], '', 1)
                if s[0] not in '0123456789':
                    result_list.append(s[0])
                    s = s.replace(s[0], '', 1)
                    wait_for_number = True
                else:
                    wait_for_number = True
            except IndexError:
                calculate = False
                break
    return result_list


s = 'les2+ 34 - 5 * 3'
s1 = '(les2+ 3) *4 - 5 * 3'
print(token_parser(s1))
