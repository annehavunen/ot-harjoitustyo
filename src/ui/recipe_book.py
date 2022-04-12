from services.recipe_service import RecipeService
from ui.print_commands import PrintCommands


class RecipeBook:
    def __init__(self):
        self.recipe_service = RecipeService()
        self.printer = PrintCommands()

    def start(self):
        print("Welcome to Recipe Book, where you can collect your favorite recipes from websites.")
        print("Categories will be added later.")
        print()
        print("Commands:")
        self.printer.print_main_commands()
        print()

        while True:
            command = input("Command: ")
            if command == "x":
                break
            if command == "1":
                self.add_recipe()
            elif command == "2":
                self.print_recipes()
            elif command == "3":
                self.open_website()
            elif command == "4":
                self.change_recipe()
            elif command == "5":
                self.remove_recipe()
            else:
                self.printer.print_main_commands()

    def add_recipe(self):
        name = input("Name of the recipe: ")
        url = input("URL of the recipe: ")
        self.recipe_service.add_recipe(name, url)

    def print_recipes(self):
        self.recipe_service.print_recipes()

    def open_website(self):
        name = input("Name of the recipe you want to open: ")
        self.recipe_service.open_recipe(name)

    def change_url(self):
        name = input("Which recipe's url do you want to change? ")
        url = input("New url: ")
        self.recipe_service.change_url(name, url)
    
    def change_name(self):
        name = input("Which recipe's name do you want to change? ")
        new_name = input("New name: ")
        self.recipe_service.change_name(name, new_name)

    def remove_recipe(self):
        name = input("Name of the recipe: ")
        self.recipe_service.remove_recipe(name)

    def change_recipe(self):
        print()
        print("Commands:")
        self.printer.print_change_commands()
        command = input("Command: ")

        if command == "r":
            print()
            self.print_commands()
        elif command == "1":
            self.change_name()
        elif command == "2":
            self.change_url()
        else:
            print()
            self.printer.print_main_commands()
