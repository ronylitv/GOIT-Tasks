class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __str__(self):
        return f'Vector({self.x},{self.y})'

v1 = Vector(10,2)
v2 = Vector(10, 3)
v3 = Vector(10,5)
print(v1 + v2 + v3)
