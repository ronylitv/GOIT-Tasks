# def get_fullname(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#
#
#     return full_name
#
#
# print(get_fullname('rostyslav', 'lytvynets', 'romanovych'))
# def first(size, *arg):
#     counter = 0
#     for i in arg:
#         counter +=1
#
#     size += counter
#
#     return size
#
#
# def second(size, *arg):
#     size += arg
#     return size
#
# print(first(1,2,3,4,5,6,6,7))



def cost_delivery(*quantity,  discount = 0):
    cost = 0
    counter = 0
    for i in quantity:

        counter += 1
        if counter == 1:
            cost += i * 5 - (i * 5) * discount
        else:
            cost += i * 2 - (i * 2) * discount


    return cost

print(cost_delivery(2, 1, 2, 3))