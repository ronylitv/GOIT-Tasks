# Создайте класс Animal. Также создайте экземпляр класса Animal и присвойте переменной animal. Для класса Animal
# в конструкторе создайте два свойства nickname - кличка животного и weight - вес животного.
# Реализуйте так же метод класса say. При реализации метода можно использовать оператор pass, пока главное это определение, а не конкретная реализация
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

a = Animal('Bonik', 32)