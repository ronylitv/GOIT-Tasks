class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass
    def change_weight(self, weight):
        self.weight = weight
    def info(self):
        print(self.weight)
        print(self.nickname)

animal = Animal("Simon", 10)
animal.change_weight(12)
animal.info()