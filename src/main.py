from os import system


def create_task():
    print('create task')


def list_task():
    print('list task')


def delete_task():
    print('delete_task')


def update_task():
    print('update task')


def print_menu():
    menu = {}
    menu['1'] = {'name': "Create Task.", 'function': create_task}
    menu['2'] = {'name': "Updated Task.", 'function': update_task}
    menu['3'] = {'name': "Delete Task.", 'function': delete_task}
    menu['4'] = {'name': "List Task.", 'function': list_task}
    menu['exit'] = {'name': "Exit"}
    options = menu.keys()
    options.sort()
    for entry in options:
        print(entry, menu[entry]['name'])
    select_user = raw_input("What would you like to do? ")
    return select_user, menu


def select_action(element_select, menu):
    select = True
    print(menu)
    while select:
        if element_select == 'exit':
            select = False
        elif element_select not in menu.keys():
            print('Select to value valid')
            loop_select()
        else:
            menu[element_select]['function']()
            loop_select()

def loop_select():
    option, menu = print_menu()
    select_action(option, menu)


if __name__ == '__main__':
    loop_select()
