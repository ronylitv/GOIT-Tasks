class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
        self.color = Animal.color

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, new_color):
        Animal.color = new_color


first_animal = Animal('Boris', 10)
first_animal.change_color('red')
second_animal = Animal('Barka', 7)





