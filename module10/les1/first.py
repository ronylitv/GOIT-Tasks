class Rectangle:
    def __init__(self, high, width):
        self.width = width
        self.height = high

    def perimeter(self):
        return 2 * (self.height + self.width)

    def square(self):
        return self.height * self.width


r = Rectangle(2, 10)
print(r.perimeter())
print(r.square())


