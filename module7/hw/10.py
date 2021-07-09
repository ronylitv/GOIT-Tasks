def make_request(keys, values):

    if len(keys) == len(values):
        json_dict = dict(zip(keys, values))
        return json_dict
    else:
        return {}




keys = ['hello', 'world', 'mama', 'tato']
values = [1,2,3,4]

print(make_request(keys, values))




