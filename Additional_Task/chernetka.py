

def real_len(text):
    new_list = ['\n', '\f', '\r', '\t', '\v']
    count = 0
    for i in text:
        if i in new_list:
            count += 1
    return len(text) - count

text = 'Hello\nWorld\v'
print(len(text))
print(real_len(text))






