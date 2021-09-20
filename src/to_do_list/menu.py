from .task import AssignmentTask
from time import sleep


class Menu:

    def __init__(self):
        self.menu = {}
        self.instance = AssignmentTask()

    def execute(self):
        self.assign_options()
        self.print_menu()

    def assign_options(self):
        self.menu['1'] = {'name': "Create Task.", 'function': self.instance.create, 'sleep_time': 2}
        self.menu['2'] = {'name': "Updated Task.", 'function': self.instance.get, 'sleep_time': 3}
        self.menu['3'] = {'name': "Delete Task.", 'function': self.instance.get, 'sleep_time': 3}
        self.menu['4'] = {'name': "List Task.", 'function': self.instance.get, 'sleep_time': 3}
        self.menu['exit'] = {'name': "Exit"}

    def print_menu(self):
        options = self.menu.keys()
        for entry in options:
            print(entry, self.menu[entry]['name'])
        select_user = input("What would you like to do? ")
        if select_user == 'exit':
            return
        elif select_user not in self.menu.keys():
            return self.print_menu()
        else:
            self.menu[select_user]['function']()
            sleep(self.menu[select_user]['sleep_time'])
            return self.print_menu()
