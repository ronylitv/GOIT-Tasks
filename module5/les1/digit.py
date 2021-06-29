numb = ['123', '456', '100', '10', '13', 'abc', '23a']


def sanitize(data):
    result = []
    for i in data:
        if i.isdigit():
            result.append(i)
    return result

def transform_to_int(data):
    result = []
    for i in data:
        if i.isdigit():
            result.append(int(i))
    return result

sanitaze_numbers = transform_to_int(numb)

srt_numb = sorted(sanitaze_numbers)

print(srt_numb, sanitaze_numbers)
