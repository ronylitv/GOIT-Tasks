from collections import UserDict, UserList, UserString


class ValueSearchableDict(UserDict):

    def has_in_keys_and_values(self, val):
        return val in self.data.values() or val in self.data.keys()


as_dict = ValueSearchableDict()

as_dict['b'] = 'a'
print(as_dict.has_in_keys_and_values('b'))
