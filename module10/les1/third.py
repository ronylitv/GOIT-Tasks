class A:
    x = 'I am A class'


class B:
    x = 'I am B class'
    y = 'I exist only in B'


class C(A, B):
    def z_print(self):
        z = "This exists only in C"
        print(z.__class__.__mro__)
    # print(self.__class__.__mro__)


c = C()
c.z_print()  # This exists only in C
print(c.y)  # I exist only in B
print(c.x)  # I am A class

