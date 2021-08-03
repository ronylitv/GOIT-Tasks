class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __repr__(self):
        return f'Vector({self.x},{self.y})'

    def __hash__(self):
        pass




a = Vector(5, 5)
b = Vector(10, 10)
print(a + b)
