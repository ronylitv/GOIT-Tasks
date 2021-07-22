def get_favorites(contacts: list):
    return [i for i in filter(lambda x: x['favorite'] == True, contacts)]


print(get_favorites([   {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.uk",
        "phone": "(992) 914-3792",
        "favorite": True,
    }
]))
