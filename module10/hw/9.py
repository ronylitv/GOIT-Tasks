from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        return list(filter(lambda x: self.data[x] == value, self.data))


c = LookUpKeyDict({'name': 'ROstyk', 'age':' 19'})
print(c.lookup_key('ROstyk'))