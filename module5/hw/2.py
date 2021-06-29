articles_dict = [
    {
        "title": "Minim voluptate eu aliqua duis pariatur cupidatat voluptate.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Dolore Lorem aliquip est labore elit labore ex consequat ad occaecat duis.",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "Aliqua minim amet ut pariatur et occaecat esse qui commodo ut duis sunt elit.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "Irure reprehenderit aliquip officia quis occaecat aute mollit laborum ullamco laboris Lorem commodo.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    coincidence = False
    new_list = []
    if letter_case:
        for i in articles_dict:
            for j in i.values():
                try:
                    if j.find(key) != -1:
                        coincidence = True
                except:
                    continue
            if coincidence:
                new_list.append(i)
            coincidence = False
    else:
        for i in articles_dict:
            for j in i.values():
                try:
                    key.upper()
                    j.upper()
                    if j.find(key) != -1:
                        coincidence = True
                except:
                    continue
            if coincidence:
                new_list.append(i)
            coincidence = False

    return new_list


print(find_articles('MInim', True))
