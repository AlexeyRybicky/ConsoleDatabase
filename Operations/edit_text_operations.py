from GUI.Viewer import enter_edit_num, enter_delete_num, print_data

from Operations.input_text_operations import enter_edit_data


def edit_data(data):
    print_data(data)
    enter_edit_num()
    edit_num = int(input())
    try:
        data['num'][edit_num] = enter_edit_data()
        print_data(data)
    except IndexError as e:
        print('Данные которые вы хотите изменить не существует')


def delete_data(data):
    print_data(data)
    enter_delete_num()
    delete_num = int(input())
    try:
        data['num'].remove(data['num'][delete_num])
        print_data(data)
    except IndexError as e:
        print('Данные которые вы хотите удалить не существует')

def enter_num_float():
    print('здесь будет функция')
