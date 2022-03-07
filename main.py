def calculate():
    number_1 = int(input('Digite o primeiro número: '))

    operation = input('Escolha a operação + - * / ')

    number_2 = int(input('Digite o segundo número: '))

    if operation == '+':
        print('= '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('= '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('= '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('= '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Valor errado, calcule novamente!.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Quer calcular novamente?
Digite S para sim e N para não.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até outra hora.')
    else:
        again()

calculate()
