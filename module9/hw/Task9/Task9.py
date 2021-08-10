COMMANDS = [
    'add',
    'change',
    'phone',
    'show all',
    'good bye',
    'close',
    'exit'
]
# if command.find('add') != -1 or command.find('change') != -1:
        #     handle_add_and_change(sep_val[1], sep_val[les2])
        # elif command.find('phone') != -1:
        #     handle_phone(sep_val[1])
        # elif command.find('show all') != -1:
        #     print(handle_show_all())
        # elif command.find("good bye") != -1 or command.find("close") != -1 or command.find("exit") != -1 or command.find('.') != -1:
        #     print('Good bye!')
        #     break
        # elif command.find('hello') != -1:
        #     print('How can I help you?')
        # else:
        #     print('Incorrect! Try again')

def add_to_file(file, *string):
    with open(file, 'a') as f:
        if type(string) == tuple:
            for i in string:
                f.write(f'{i}\n')
        else:
            f.write(f'{string}\n')


def change_file(file, string: str):
    input_name = string.split(' ')[0]
    rewrite_list = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for item in lines:
            name = item.split(' ')
            if name[0] == input_name:
                rewrite_list.append(string + '\n')
            else:
                rewrite_list.append(item)
    with open(file, 'w') as f:
        for item in rewrite_list:
            f.write(item)


def phone_find(file, name):
    with open(file, 'r') as f:
        lines = f.readlines()
        for item in lines:
            if item.split(' ')[0] == name:
                return item.split(' ')[1].strip()


def show_all(file):
    with open(file, 'r') as f:
        for item in f.readlines():
            print(item.strip())

