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

categories = {
    "1": "1 meat and poultry",
    "2": "2 seafood",
    "3": "3 vegetarian",
    "4": "4 snacks and side dishes",
    "5": "5 desserts",
    "6": "6 baking",
    "7": "7 other"
}

printing_options = {
    "r" : "r return",
    "1": "1 print all",
    "2": "2 print by category"
}

class PrintCommands:
    def print_main_commands(self):
        for command in main_commands.values():
            print(command)

    def print_change_commands(self):
        for command in change_commands.values():
            print(command)

    def print_categories(self):
        for command in categories.values():
            print(command)

    def print_printing_options(self):
        for command in printing_options.values():
            print(command)

    def categories(self):
        return len(categories)
