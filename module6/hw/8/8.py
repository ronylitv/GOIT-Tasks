def save_applicant_data(source, output):
    with open(output, 'w') as f:
        sent = ''
        for el in source:
            new_list = []
            for ind, val in el.items():
                new_list.append(str(val))
            sent += ','.join(new_list) + '\n'
        f.write(sent)


source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

save_applicant_data(source, 'output.txt')
