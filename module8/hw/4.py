from random import randrange


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < min or quantity > max:
        return []
    ticket_numbers = set()
    while len(ticket_numbers) != quantity:
        ticket_numbers.add(randrange(min, max))
    return sorted(list(ticket_numbers))

numb_list = get_numbers_ticket(1, 21, 22)
print(numb_list)
print(type(numb_list))
print(f'Lenght: {len(numb_list)}\nTicket_numbers: {numb_list}')


