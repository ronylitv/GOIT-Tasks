import re

CONTACTS_DICT = {}


def input_error(func):
    def inner(*args):
        if 1 < len(args) <= 2:
            result = re.search(r'\+?380\d+|0\d+', args[1])
            if not args[0].isalpha():
                print('Enter correct username!')
            if result:
                if len(args[1]) != len(result.group()) or len(args[1]) < 10:
                    print('Enter correct number!')
                else:
                    func(args[0], args[1])
            else:
                print('Enter correct number!')
        else:
            if not args[0] in CONTACTS_DICT.keys():
                print('Contact does not exist!')
            else:
                print(func(args[0]))

    return inner


@input_error
def handle_add_and_change(name, contact):
    CONTACTS_DICT[name] = contact


@input_error
def handle_phone(name):
    return CONTACTS_DICT[name]


def handle_show_all():
    return CONTACTS_DICT


def main():
    while True:
        command = input('Command: ').lower()
        sep_val = command.split(' ')
        if sep_val[0] == 'add' and len(sep_val) > 2 or sep_val[0] == 'change' and len(sep_val) > 2:
            handle_add_and_change(sep_val[1].title(), sep_val[2])
        elif sep_val[0] == 'phone':
            handle_phone(sep_val[1].title())
        elif sep_val[0] == 'show' and sep_val[1] == 'all':
            print(handle_show_all())
        elif sep_val[0] in ['good bye', "close", "exit", '.']:
            print('Good bye!')
            break
        elif sep_val[0] == 'hello':
            print('How can I help you?')
        else:
            print('Incorrect! Try again')


main()