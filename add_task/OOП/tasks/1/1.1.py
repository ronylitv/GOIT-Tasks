import csv


class Phones:
    def __init__(self, path):
        self.path = path

    def list_numbers(self):
        with open(self.path, 'r') as file:
            lines = file.readlines()
            number_list = [i.split(';')[3].strip() for i in lines[1:]]
            return number_list

    @staticmethod
    def remove_prefix(num_list: list):
        return [i.removeprefix('38') for i in num_list]

    @staticmethod
    def del_zero(num_list: list):
        return [i.removeprefix('0') if i.startswith('00') else i for i in num_list]

    @staticmethod
    def del_duplicates(num_list: list):
        return set(num_list)

    @staticmethod
    def invalid_number(num_list: list):
        return [i for i in num_list if len(i) != 10]

    @staticmethod
    def find_intersections(path_first, path_second):
        with open(path_first, 'r') as file1:
            lines = file1.readlines()
            phone_list1 = [i.split(';;;')[1].removesuffix(';;\n') for i in lines]
        phone_list2 = Phones(path_second).list_numbers()
        return list(set(phone_list1) & set(phone_list2))[1:]

    @staticmethod
    def inner_values_rec(path_first, path_second):
        with open(path_first, 'r') as file1:
            lines = file1.readlines()
            phone_list1 = [i.split(';;;')[1].removesuffix(';;\n') for i in lines if
                           i.split(';;;')[1].removesuffix(';;\n').startswith('380')]
        phone_list2 = Phones(path_second).list_numbers()
        values = list(set(phone_list1) - set(phone_list2))[1:]
        with open(f'individual_elements_{path_first}', 'w', encoding='utf-8') as csvfile:
            file_writer = csv.DictWriter(csvfile, delimiter=',', lineterminator="\r", fieldnames=['Phone'])
            file_writer.writeheader()
            for item in values:
                file_writer.writerow({'Phone': item})

    @staticmethod
    def outer_values_rec(path_first, path_second):
        with open(path_first, 'r') as file1:
            lines = file1.readlines()
            phone_list1 = [i.split(';;;')[1].removesuffix(';;\n') for i in lines if
                           i.split(';;;')[1].removesuffix(';;\n').startswith('380')]
        phone_list2 = Phones(path_second).list_numbers()
        values = list(set(phone_list2) - set(phone_list1))[1:]
        with open(f'individual_elements_{path_second}', 'w', encoding='utf-8') as csvfile:
            file_writer = csv.DictWriter(csvfile, delimiter=',', lineterminator="\r", fieldnames=['Phone'])
            file_writer.writeheader()
            for item in values:
                file_writer.writerow({'Phone': item})

    @staticmethod
    def sort_operators(first_phone_list: list, second_phone_list: list):
        combine_list = first_phone_list + second_phone_list

        def add_dash(rand_list, quantity_dash):
            return rand_list + quantity_dash * ['-']

        kyivstar = []
        vodafone = []
        lifecell = []
        other = []
        for item in combine_list:
            if item[:3] in ['067', '068', '096', '097', '098']:
                kyivstar.append(item)
            elif item[:3] in ['050', '066', '095', '099']:
                vodafone.append(item)
            elif item[:3] in ['063', '073', '093']:
                lifecell.append(item)
            else:
                other.append(item)
        with open('Phones_table.md', 'w') as new_file:
            max_len = len(max(kyivstar, vodafone, lifecell, other))
            k = add_dash(kyivstar, max_len - len(kyivstar))
            v = add_dash(vodafone, max_len - len(vodafone))
            l = add_dash(lifecell, max_len - len(lifecell))
            o = add_dash(other, max_len - len(other))
            temp = '## Table of Phones\n'
            temp += '|{:^20}|{:^20}|{:^20}|{:^20}|\n'.format('Kyivstar', 'Vodafone', 'Lifecell', 'Other')
            temp += '|{0:^20}|{0:^20}|{0:^20}|{0:^20}|\n'.format('-' * 20)
            for i in range(max_len):
                temp += '|{:^20}|{:^20}|{:^20}|{:^20}|\n'.format(k[i], v[i], l[i], o[i])
            new_file.write(temp)

    @staticmethod
    def add_to_file(phone_list: list, filename):
        with open(filename, 'a') as file:
            for i in phone_list:
                file.write(i + '\n')




# file = Phones('text.txt')
# phones = file.list_numbers()
# san_phones = file.remove_prefix(phones)
# zer_er = file.del_zero(san_phones)
# set_numbers = file.del_duplicates(zer_er)
# invalid_numbers = file.invalid_number(zer_er)
# print(Phones.find_intersections('bot.csv', 'in_zohot.csv'))
# Phones.inner_values_rec('bot.csv', 'in_zohot.csv')
# Phones.outer_values_rec('bot.csv', 'in_zohot.csv')
p = []
l = []
with open('individual_elements_bot.csv', 'r') as f:
    lines = f.readlines()[1:]
    san_lines = Phones.remove_prefix([i.strip() for i in lines])
    p.extend(san_lines)

with open('individual_elements_in_zohot.csv', 'r') as file:
    lines1 = file.readlines()[1:]
    san_lines1 = Phones.remove_prefix([i.strip() for i in lines1])
    l.extend(san_lines1)
#
# Phones.sort_operators(p, l)

Phones.add_to_file(p, 'example.csv')
