import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    cats_list = []
    if isinstance(cats[0], dict):
        for i in cats:
            p = Cat(**i)
            cats_list.append(p)
        return cats_list

    else:
        for el in cats:
            cats_dict = el._asdict()
            cats_list.append(cats_dict)

        return cats_list



print(convert_list([Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]))
print(convert_list([
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]))