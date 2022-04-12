main_commands = {
    "x": "x exit",
    "1": "1 add a recipe",
    "2": "2 print recipes",
    "3": "3 open a recipe",
    "4": "4 change a recipe",
    "5": "5 remove a recipe"
}

change_commands = {
    "r": "r return",
    "1": "1 change a recipe's name",
    "2": "2 change a recipe's url"
}

class PrintCommands:
    def print_main_commands(self):
        for command in main_commands.values():
            print(command)
    def print_change_commands(self):
        for command in change_commands.values():
            print(command)
