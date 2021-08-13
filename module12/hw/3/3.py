import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'email', 'phone', 'favorite'])
        writer.writeheader()
        for item in contacts:
            writer.writerow({'name':item['name'], 'email': item['email'],
                             'phone': item['phone'], 'favorite': item['favorite']})


def read_contacts_from_file(filename):
    with open(filename, 'r') as csvfile:
        contacts = []
        reader = csv.DictReader(csvfile)
        for item in reader:
            contacts.append({
                'name': item['name'],
                'email': item['email'],
                'phone': item['phone'],
                'favorite': False if item['favorite'] == 'False' else True
            })
        return contacts


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

write_contacts_to_file('pol', l)
print(read_contacts_from_file('pol'))









