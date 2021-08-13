import pickle


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f'HELLO IM {self.name}')


def main():
    # bob = Human('Bob', 23)
    # with open('bob.dat', 'wb') as f:
    #     pickle.dump(bob, f)
    with open('bob.dat', 'rb') as f:
        bob = pickle.load(f)
        bob.greeting()
        print(type(bob))


if __name__ == '__main__':
    main()
