import random
import sys

class RandPhone:
    def __init__(self, list_phone: list):
        self.list_phone = list_phone

    def rand_phones(self, quantity):
        return random.sample(self.list_phone, quantity)

    def r_list(self, working_list):
        intersect = list(set(self.list_phone) & set(working_list))
        rand_intersect = random.sample(intersect, random.randrange(0, len(intersect) + 1))
        if rand_intersect in self.list_phone:
            self.list_phone.remove(rand_intersect)
        return rand_intersect + self.list_phone

    def rand_list(self, random_list):
        intersect = list(set(self.list_phone) & set(random_list))
        rand_intersect = random.sample(intersect, random.randrange(0, len(intersect) + 1))
        if rand_intersect in self.list_phone:
            self.list_phone.remove(rand_intersect)
        return rand_intersect + random.sample(self.list_phone, random.randrange(0, len(self.list_phone) + 1))

    @staticmethod
    def reg_percentage(reg_phone, event_phone):
        intersect_reg_visit = list(set(reg_phone) & set(event_phone))

        return f'Percentage of registered and was on event {(len(intersect_reg_visit)/len(set(event_phone)))*100}%'

    @staticmethod
    def output_phone(first_list, second_list, flag):
        if flag == '0':
            return first_list + list(set(second_list) - set(first_list))
        elif flag == '1':
            return list(set(first_list) & set(second_list))
        elif flag == 'les2':
            return list(set(first_list) & set(second_list))
        elif flag == '3':
            return RandPhone.reg_percentage(first_list, second_list)
        elif flag == '4':
            intersect_reg_visit = (set(first_list) & set(second_list))
            intersect_noreg_visit = set(intersect_reg_visit) ^ set(second_list)
            return f'Was not registered, but visited the event {(len(intersect_noreg_visit)/len(set(second_list)))*100}%'


with open('individual_elements_bot.csv', 'r') as file:
    lines = file.readlines()
    l = [i.strip() for i in lines[1:]]
with open('individual_elements_in_zohot.csv', 'r') as next_file:
    lines1 = next_file.readlines()
    l1 = [i.strip() for i in lines1[1:]]

r = RandPhone(l)
random_phone = r.rand_phones(20)
r1 = RandPhone(random_phone)
r_list = r1.r_list(l1)
r2 = RandPhone(r_list)
rand_list = r2.rand_list(l)
print(RandPhone.reg_percentage(l, l1))
p = RandPhone.output_phone(l, l1, '4')
print(p)
# reg = ['380954782633','380970179448','380930058790','380967058696','380509864910','380504947306','380978542274',
#        '380935989893']
# visit = ['380954782633','380970179448','380930058790','380967058696', '380675114311','380666057637','380982130444'
#     ,'380958128837']
# right_ans = ['380675114311','380666057637','380982130444','380958128837']
#
# a = (set(reg) & set(visit))
# print(a)
# print(list(set(reg) & set(visit)))
# print(list(a ^ set(visit)))
