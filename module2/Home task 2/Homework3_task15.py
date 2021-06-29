result = None
operand = None
operator = None
wait_for_number = True
loop = True
calculate = True

while calculate:
    while wait_for_number:
        try:
            operand = int(input('Number: '))
        except ValueError:
            print('Invalid symbol. Try again')
            continue

        if operator == '+':
            result += operand
            operand = None

        elif operator == '/':
            result /= operand
            operand = None

        elif operator == '-':
            result -= operand
            operand = None

        elif operator == '*':
            result *= operand
            operand = None

        wait_for_number = False
    while not wait_for_number:
        operator = input('Operator: ')
        if operator == '+':
            wait_for_number = True

        elif operator == '/':
            wait_for_number = True

        elif operator == '-':
            wait_for_number = True

        elif operator == '*':
            wait_for_number = True

        elif operator == '=' or operand == '=':
            print(result)
            calculate = False
            break

        else:
            print(f'Your symbol {operator} is not operator. Try again')
            wait_for_number = False

    while loop:
        result = operand
        operand = None
        loop = False
