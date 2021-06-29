result = None
operand = None
operator = None
wait_for_number = True
one_time_loop = True
a = 0
b = True

while True:
    while wait_for_number:
        try:
            operand = int(input('Number: '))
            wait_for_number = False
        except ValueError:
            print(f'Operand {operand} is not a number. Try again')
            continue
    while not wait_for_number:
        while b:
            operator = input('Operator: ')
            b = False

        while a > 0:

            try:

                if operator == '+':
                    result += operand
                    operand = None
                    a = 0

                elif operator == '-':
                    result -= operand
                    operand = None
                    a = 0
                elif operator == '*':
                    result *= operand
                    operand = None
                    a = 0
                elif operator == '/':
                    result /= operand
                    operand = None
                    a = 0
                else:
                    print(f'Operator {operator} isn`t valid. Try again')
            except ValueError:
                print(f'Operator {operator} isn`t valid. Try again')
                continue
            operator = input('Operator: ')


        a = 1
        print(result)

        while one_time_loop:
            result = operand
            one_time_loop = False
        wait_for_number = True
