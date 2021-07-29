class MyClass:
    name = 'John'
    def say_name(self):
        print(f'Hi! My name is {self.name}')


class YourClass:
    def do_something(self, obj):
        obj.say_name()


YourClass().do_something(MyClass())
