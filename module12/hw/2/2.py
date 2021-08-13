import json


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w') as f:
        json.dump({'contacts': contacts}, f)


def read_contacts_from_file(filename):
    with open(filename, 'r') as f:
        unpacked = json.load(f)
        return unpacked['contacts']

p = {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
p1 = {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-4792",
    "favorite": False,
}
l = [p, p1]
write_contacts_to_file('kok', l)
print(read_contacts_from_file('kok'))