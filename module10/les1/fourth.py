from cmath import pi
class Figure:
    def __init__(self, sides: list, radius=0):
        self.side = sides
        self.radius = radius


class Triangle(Figure):
    def square(self):
        if len(self.side) != 3:
            raise ValueError
        return 0.5 * self.side[0] * self.side[1]

    def perimetr(self):
        return sum(self.side)


class Circle(Figure):
    def square(self):
        return pi * (self.radius ** 2)


class Rectangular(Figure):
    def square(self):
        if len(self.side) != 4:
            raise ValueError
        return self.side[0] * self.side[1]

    def perimetr(self):
        return sum(self.side)


c = Circle([], 6)
print(c.square())
