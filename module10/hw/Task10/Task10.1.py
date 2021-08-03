from collections import UserDict
import re


class Field:
    pass


class Phone(Field):
    def __init__(self, *phone):
        self.phone = [i for i in phone]

    def check_phone(self):
        result = re.search(r'\+?380\d+|0\d+', self.phone[0][0])
        if result:
            if not len(result.group()) == len(self.phone[0]):
                self.phone[0] = ''
        else:
            print('Enter correct number!')
            self.phone[0] = ''

        for item in self.phone[0][1:]:
            res = re.search(r'\w+@\w+.\w{3}', item)
            if res:
                if len(res.group()) != len(item):
                    self.phone.remove(item)
            else:
                self.phone.remove(item)
        return self.phone

    def __str__(self):
        return f'{self.phone}'


class Name(Field):
    def __init__(self, name):
        self.name = name

    def check_name(self):
        if not self.name.isalpha():
            print('Enter correct username!')
        else:
            return self.name

    def __str__(self):
        return f'{self.name}'


class Record:
    def __init__(self, name, phone):
        self.name = Name(name).check_name()
        self.phone = phone
        if type(self.phone) == list:
            temp = []
            for item in self.phone:
                for j in item:
                    temp.append(j)
            self.phone = temp

    def __str__(self):
        return f'{self.name},{self.phone}'


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.__str__()] = record.__str__()
        if 'None' in self.data.keys():
            self.data.pop('None')

    def change_phone(self, name, *phone):
        self.data[name] = f'{name},{[i for i in phone]}'

    def find_phone(self, name):
        if name in self.data.keys():
            value = self.data[name]
            res = re.search(r'\+\d+', value)
            return res.group()
        return "Does not exist in database!"


def main():
    main_address_book = AddressBook()
    while True:
        command = input('Command: ').lower()
        sep_val = command.split(' ')
        if sep_val[0] == 'add' and len(sep_val) > 2:
            main_address_book.add_record(Record(sep_val[1].title(), Phone(sep_val[2:]).check_phone()))
        elif sep_val[0] == 'change' and len(sep_val) > 2:
            main_address_book.change_phone(sep_val[1].title(), sep_val[2])
        elif sep_val[0] == 'phone':
            print(main_address_book.find_phone(sep_val[1].title()))
        elif sep_val[0] == 'show' and sep_val[1] == 'all':
            print(main_address_book)
        elif sep_val[0] in ['good bye', "close", "exit", '.']:
            print('Good bye!')
            break
        elif sep_val[0] == 'hello':
            print('How can I help you?')
        else:
            print('Incorrect! Try again')


if __name__ == '__main__':
    main()
