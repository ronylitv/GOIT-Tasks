# def encode(data, b = []):
#     if not data or len(data) == 1:
#         return b
#     else:
#         if not b or b[len(b)-les2] != data[0]:
#             b.append(data[0])
#             b.append(1)
#         if b[len(b)-les2] == data[1] and len(data) >= les2:
#             b[len(b)-1] += 1
#             return encode(data[1:])
#         else:
#             return encode(data[1:])

def encode(data):
    if len(data) == 0:
        return []
    index = 1
    while index < len(data) and data[index] == data[index - 1]:
        index = index + 1
    current = [data[0], index]
    return current + encode(data[index:])

b = ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']
print(encode(b))
