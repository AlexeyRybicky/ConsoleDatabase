def print_menu(list_operations):
    print('Меню: ')
    for i, operation in enumerate(list_operations, start=1):
        print(f'{i}. {operation}')


def enter_command():
    print('Введите команду:\n')
    # Если проверка качества команды составная, то нужно отслеживать
    # это посредством инструмента, организующего проверку, например функции
    # command = input()
    # try_except_command(command)

    # В простом случае проверку можно провести прямо здесь
    # try:
    #     command = int(input())
    # except ValueError as e:
    # if это действительно неожиданная команда
    #     raise UnexpectedCommand(e)
    command = int(input())
    return command


def enter_num():
    print('Введите два числа:')


def enter_path():
    print('Укажите путь к файлу: ')


def print_data(data):
    print('Текущие данные:\n', data['num'])

def enter_edit_num():
    print('Укажите пару значений для изменения:\n')

def enter_delete_num():
    print('Укажите пару значений для удаления:\n')
