from GUI.Viewer import enter_num, enter_path

import pandas as pd


def controll_enter_num(data):
    a, b = None, None
    while True:
        try:
            enter_num()
            a, b = int(input()), int(input())
            break
        except ValueError as e:
            print('Введен некорректный тип\n')

    modul_enter_num(data, a, b)


def modul_enter_num(data, a, b):
    data['num'].append([a, b])


def enter_edit_data():
    a, b = None, None
    while True:
        try:
            enter_num()
            a, b = int(input()), int(input())
            return [a, b]
        except ValueError as e:
            print('Введен некорректный тип\n')


def enter_from_excel(data):
    enter_path()
    file_path = input()
    try:
        excel_file = pd.read_excel(file_path, header=None)  # закрывается ли файл после чтения?
        for i, row in excel_file.iterrows():
            data['num'].append([row[0], row[1]])
    except FileNotFoundError as e:
        print(f'Файл {file_path} не найден')
    except OSError as e:
        print(f'Путь {file_path} указан неверно')


def enter_from_txt(data):
    enter_path()
    file_path = input()
    try:
        with open(file_path, 'r') as txt_file:
            for line in txt_file:
                data['num'].append([int(x) for x in line.split()])
    except FileNotFoundError as e:
        print(f'Файл {file_path} не найден')
    except OSError as e:
        print(f'Путь {file_path} указан неверно')


def enter_from_csv(data):
    enter_path()
    file_path = input()
    try:
        with open(file_path, 'r') as csv_file:
            for line in csv_file:
                data['num'].append(list(map(int, line.split(';'))))
    except FileNotFoundError as e:
        print(f'Файл {file_path} не найден')
    except OSError as e:
        print(f'Путь {file_path} указан неверно')
