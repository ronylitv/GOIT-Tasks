import re


def generator_numbers(string=""):
    while True:
        gen_numbers = re.search(r'\d+', string)
        if not gen_numbers:
            break
        string = string[string.find(gen_numbers.group()) + len(gen_numbers.group()):]
        yield gen_numbers.group()


def sum_profit(string):
    number_values = [int(i) for i in generator_numbers(string)]
    return sum(number_values)


print(sum_profit("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, "
                 "and the king gave $1000."))

