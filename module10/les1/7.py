class Mammal:
    phrase = ''
    def voice(self):
        return self.phrase


class Dog(Mammal):
    phrase = 'Bark!'



class Cat(Mammal):
    phrase = 'Meow!'


class Chupakabra:
    def voice(self):
        return 'Whooooo!!!'

class Person(Mammal):
    phrase = 'HI!'
class Recorder:
    def record_animal(self, animal):
        voice = animal.voice()
        print(f'Recorded "{voice}"')


r = Recorder()
cat = Cat()
dog = Dog()
person = Person()
strange_animal = Chupakabra()

r.record_animal(cat)            # Recorded "Meow!"
r.record_animal(dog)            # Recorded "Bark!"
r.record_animal(strange_animal) # Recorded "Whooooo!!!"
r.record_animal(person)