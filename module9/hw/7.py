def normal_name(list_name):
    return [i for i in map(lambda x: x.title(), list_name)]

print(normal_name(["dan", "jane", "steve", "mike"]))