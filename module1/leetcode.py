from tkinter import Tk, Button


class Verification:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError('Weak password')

    def save(self):
        with open('users.txt', 'a') as r:
            r.write(f'{self.login, self.password}' + '\n')

class My_App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry('400x400')
        self.setUI()

    def setUI(self):
        Button(self, text='OK').pack()

class V2(Verification):

    def __init__(self, login, password, age):
        super().__init__(login, password)
        self.__save()
        self.age = age

    def __save(self):
        with open('users.txt', 'r') as r:
            for i in r:
                if f'{self.login, self.password}' + '\n' == i:
                    raise ValueError('It exists!')
        super().save()

    def show(self):
        return self.password, self.login

x = V2('bob', '11111111111', 23)
