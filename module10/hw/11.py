from collections import UserString


class NumberString(UserString):
    def number_count(self):
        return len(list(filter(lambda x: x.isdigit(), self.data)))


c = NumberString('lsdfsdlkf123456')
print(c.number_count())




