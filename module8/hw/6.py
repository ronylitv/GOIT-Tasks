from decimal import Decimal, getcontext


# def decimal_average(number_list, signs_count):
#     getcontext().prec = signs_count
#     return Decimal(sum(number_list))/Decimal(len(number_list))

# def decimal_average(number_list, signs_count):
#     summ = 0
#     getcontext().prec = signs_count
#     for numb in number_list:
#         summ += Decimal(numb) / Decimal(len(number_list))
#     return summ



def decimal_average(number_list, signs_count):
    dec_list = [Decimal(i) for i in number_list]
    getcontext().prec = signs_count
    average = sum(dec_list) / Decimal(len(dec_list))
    return average



k = [31, 55, 177, 2300, 1.57]
list = [Decimal(i) for i in k]
average = sum(list) / Decimal(len(list))
print(list)
print(average)

print(decimal_average([31, 55, 177, 2300, 1.57], 9))

