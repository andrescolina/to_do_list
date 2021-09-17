from .task import AssignmentTask
from time import sleep


class Menu:

    def __init__(self):
        self.menu = {}
        self.instance = AssignmentTask()

    def execute(self):
        select = self.print_menu()
        self.select_action(select)

    def print_menu(self):
        self.menu['1'] = {'name': "Create Task.", 'function': self.instance.create, 'sleep_time': 2}
        self.menu['2'] = {'name': "Updated Task.", 'function': self.instance.get, 'sleep_time': 3}
        self.menu['3'] = {'name': "Delete Task.", 'function': self.instance.get, 'sleep_time': 3}
        self.menu['4'] = {'name': "List Task.", 'function': self.instance.get, 'sleep_time': 3}
        self.menu['exit'] = {'name': "Exit"}
        options = self.menu.keys()
        for entry in options:
            print(entry, self.menu[entry]['name'])
        select_user = input("What would you like to do? ")
        return select_user

    def select_action(self, element_select):
        if element_select == 'exit':
            return
        elif element_select not in self.menu.keys():
            self.execute()
        else:
            self.menu[element_select]['function']()
            sleep(self.menu[element_select]['sleep_time'])
            self.execute()
