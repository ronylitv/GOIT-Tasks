import base64
from newtop import get_credentials_users
data = get_credentials_users('file_bit.txt')
def encode_data_to_base64(data):
    base64_list = []
    for el in data:
        message_bytes = el.encode('utf-8')
        base64_code = base64.b64encode(message_bytes)
        base64_mes = base64_code.decode('utf-8')
        base64_list.append(base64_mes)
    return base64_list

print(encode_data_to_base64(data))



