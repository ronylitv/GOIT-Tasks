stroka = 'Say hi i love [stroka grupy] lambda ya lubly [tebe]'

# test = 'love [stroka grupy] lambda'
# start_index = test.find('[')
# end_index = test.find(']')
#
# print(start_index, end_index)
#
# new_str = test[:start_index] + test[end_index + 2:]
# print(new_str)


def sanitize(data):
    new_string = data[:]
    while True:
        start_index = new_string.find('[')
        end_index = new_string.find(']')
        if start_index == -1:
            break
        new_string = new_string[:start_index] + new_string[end_index + 2:]
    return new_string


print(sanitize(stroka))
