def get_grade(key):
    try:
        grade = {'F': 1, 'FX': 2, 'E': 3, 'D': 3, 'C': 4, 'B': 5, 'A': 5}
        val = grade[key]
        return val
    except:
        return

def get_description(key):
    try:
        grade = {'F': 'неудовлетворительно', 'FX': 'неудовлетворительно', 'E': 'достаточно',
                 'D': 'удовлетворительно', 'C': 'хорошо', 'B': 'очень хорошо',
                 'A': 'отлично'}
        val = grade[key]
        return val
    except:
        return

print(get_grade('AA'))

