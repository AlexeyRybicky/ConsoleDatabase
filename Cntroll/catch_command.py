def catch_command(command_number, data):
    # list_operations = menu_conversion(operations)
    try:
        current_menu = data['operations']["current_menu"]
        list_operations = list(data['operations'][current_menu].keys())
        command = list_operations[command_number - 1]
        data['operations'][current_menu][command](data)
    except KeyError as e:
        print('Cначала необходимо ввести 2 числа\n')
    except IndexError as e:
        print('Такой команды не существует\n')


def switch_input_text(data):
    data['operations']["current_menu"] = 'input_text'


def switch_output_text(data):
    data['operations']["current_menu"] = 'output_text'


def switch_edit_text(data):
    data['operations']["current_menu"] = 'edit_text'


def switch_main_menu(data):
    data['operations']["current_menu"] = 'main'
