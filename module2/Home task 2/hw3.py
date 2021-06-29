# result = None
# operand1 = None
# operand2 = None
# operator = None
# equal = None
# wait_for_number = True
#
# while not operand1:
#     try:
#         operand1 = int(input("Enter your first number: "))
#
#     except ValueError:
#         print("Is not a number. Try again")
#
# while not operand2:
#     try:
#         operand2 = int(input("Enter your second number: "))
#
#     except ValueError:
#         print("Is not a number. Try again")
#
# while True:
#     operator = input('Put your operator: ')
#
#     if operator == "+":
#         result = operand2 + operand1
#         break
#
#     elif operator == '-':
#         result = operand2 - operand1
#         break
#
#     elif operator == '/':
#         result = operand2 / operand1
#         break
#
#     elif operator == '*':
#         result = operand2 * operand1
#         break
#
#     else:
#         print(f'Your symbol {operator} isn`t operator - try again')
#
# while wait_for_number:
#
#     equal = input('Please enter "=" to calculate your example: ')
#     if equal != '=':
#         print('Try again')
#         continue
#
#     else:
#         print(result)
#         wait_for_number = False



# 'Spwwz xj wteewp qctpyod!' offset=37


# Тестовое сообщение закодировано неверно! 'Hello my little friends!' -> 'Spwwz xj wteewp qctpyod!' offset=37
message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""

for ch in message:
    if ch in 'qwertyuiopasdfghjklzxcvbnm':
        pos = ord(ch) - ord('a')
        pos = (pos + offset) % 26
        encoded_message += chr(pos + ord("a"))
    elif ch == ' ':
        encoded_message += ' '
    elif ch == '!':
        encoded_message += '!'
    else:
        ch = ch.lower()
        pos = ord(ch) - ord('a')
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("a"))
        new_char = new_char.upper()
        encoded_message += new_char

print(encoded_message)
