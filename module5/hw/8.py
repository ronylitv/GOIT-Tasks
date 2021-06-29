grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    count = 0
    new_list = []
    for el, val in students.items():
        count += 1
        s = '{:>4}|{:<10}|{:^5}|{:^5}'.format(count, el, val, grade[val])
        new_list.append(s)
    return new_list


students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

print(formatted_grades(students))







