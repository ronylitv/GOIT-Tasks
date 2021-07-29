def get_emails(list_contacts: list):
    return [i for i in map(lambda x: x['email'], list_contacts)]

email = [{
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }
]

print(get_emails(email))
