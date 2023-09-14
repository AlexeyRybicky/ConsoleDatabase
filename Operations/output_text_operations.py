def print_summ(data):
    for a, b in data['num']:
        print(f'{a} + {b} = {a + b}')


def print_residual(data):
    for a, b in data['num']:
        print(f'{a} - {b} = {a - b}')


def print_multiplication(data):
    for a, b in data['num']:
        print(f'{a} * {b} = {a * b}')


def print_private(data):
    try:
        for a, b in data['num']:
            print(f'{a} : {b} = {a / b}')
    except ZeroDivisionError as e:
        print('НА 0 ДЕЛИТЬ НННННЕЕЕЕЕЛЛЬЬЬЬЗЗЗЯЯЯЯ')


def print_enter_number(data):
    print('Вы ввели:')
    for a, b in data['num']:
        print(f'{a} и {b}')
