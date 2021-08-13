import pickle
#
#
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __getstate__(self):
#         return {
#             'name': self.name,
#             'age': self.age
#         }
#
#     def __setstate__(self, state):
#
#
# bob = Human('Bob', 23)
# with open('pop', 'wb') as f:
#     pickle.dump(bob, f)
#
# with open('pop', 'rb') as file:
#     print(pickle.load(file))
class Foo(object):
    def __init__(self, val=2):
        self.val = val

    def __getstate__(self):
        print("I'm being pickled")
        self.val *= 2
        return self.__dict__

    def __setstate__(self, d):
        print("I'm being unpickled with these values: " + repr(d))
        self.__dict__ = d
        self.val *= 3


f = Foo()
f_data = pickle.dumps(f)
f_new = pickle.loads(f_data)
