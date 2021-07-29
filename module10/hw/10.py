from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        return sum([i for i in self.data if i > 0])


l = AmountPaymentList([1, -3, 4])
print(l.amount_payment())