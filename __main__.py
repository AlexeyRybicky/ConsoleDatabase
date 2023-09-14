from GUI.Viewer import print_menu, enter_command

from Cntroll.catch_command import (catch_command, switch_input_text, switch_output_text,
                                   switch_edit_text, switch_main_menu)

from Operations.input_text_operations import (controll_enter_num, enter_from_excel,
                                              enter_from_txt, enter_from_csv)

from Operations.output_text_operations import (print_summ, print_residual,
                                               print_multiplication, print_private,
                                               print_enter_number)

from Operations.edit_text_operations import edit_data, delete_data, enter_num_float

import sys


class UnexpectedCommand(ValueError):
    ...


def run():
    data = {}
    data['num'] = []
    data['operations'] = {"current_menu": "main"}

    data['operations']['main'] = {
        'Ввод данных': switch_input_text,
        'Вывод результата': switch_output_text,
        'Редактирование': switch_edit_text,
        'Выход из программы': exit_program
    }

    data['operations']['input_text'] = {
        'Ввести числа': controll_enter_num,
        'Ввести из Excel': enter_from_excel,
        'Ввести из TXT': enter_from_txt,
        'Ввести из CSV': enter_from_csv,
        'Назад': switch_main_menu
    }

    data['operations']['output_text'] = {
        'Вывести сумму': print_summ,
        'Вывести разность': print_residual,
        'Вывести произведение': print_multiplication,
        'Вывести частное': print_private,
        'Вывести данные': print_enter_number,
        'Назад': switch_main_menu
    }

    data['operations']['edit_text'] = {
        'Изменить данные': edit_data,
        'Удалить данные': delete_data,
        'Указать кол-во знаков после запятой': enter_num_float,
        'Назад': switch_main_menu
    }
    while True:
        # list_operations = menu_conversion(data['operations'])
        while True:
            try:
                current_menu = data['operations']["current_menu"]
                print_menu(list(data['operations'][current_menu].keys()))
                command = enter_command()
                break
            except ValueError as e:
                print('Введен некорректный тип\n')
        catch_command(command, data)


def exit_program(data):
    print('Программа завершена\n')
    sys.exit(0)


run()
