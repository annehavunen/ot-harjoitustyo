main_commands = {
    "x": "x exit",
    "1": "1 add a recipe",
    "2": "2 print recipes",
    "3": "3 open a recipe",
    "4": "4 change a recipe",
    "5": "5 remove a recipe",
    "6": "6 category test", # testausta...
    "7": "7 print category test",
    "8": "8 print recipe_id test"
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
    "7": "7 other" # ehkä vielä 1-2 kategoriaa
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