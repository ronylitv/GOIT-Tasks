source1 = [
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


def save_applicant_data(source, output):

    with open(output, 'w') as f:
        write_to_file = ''
        for i in source:
            data = []
            for value in i.values():
                data.append(str(value))
            write_to_file += ','.join(data) + '\n'
        f.write(write_to_file)


save_applicant_data(source1, 'output.txt')
