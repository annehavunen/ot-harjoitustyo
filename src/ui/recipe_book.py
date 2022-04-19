from services.recipe_service import RecipeService
from ui.print_commands import PrintCommands


class RecipeBook:
    def __init__(self):
        self.recipe_service = RecipeService()
        self.printer = PrintCommands()

    def start(self):
        print("Welcome to Recipe Book, where you can collect your favorite recipes from websites.")
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
        name = input("Name of the recipe (return with 'enter'): ")
        if name != "":
            url = input("URL of the recipe: ")
            recipe_id = self.recipe_service.add_recipe(name, url)
            if recipe_id:
                print("Write the numbers of the categories without spaces.")
                print("For example: 123")
                self.printer.print_categories()
                types = input("Categories of the recipe: ")
                self.recipe_service.add_categories(recipe_id, types)
                print("Recipe added")
            else:
                print(f"Recipe with the name {name} exists already.")
        print()
        self.printer.print_main_commands()

    def open_website(self):
        name = input("Name of the recipe you want to open (return with 'enter'): ")
        if name != "":
            exist = self.recipe_service.open_recipe(name)
            if not exist:
                print(f"There is no recipe called {name}")
        print()
        self.printer.print_main_commands()

    def change_recipe(self):
        print()
        print("Commands:")
        self.printer.print_change_commands()
        command = input("Command: ")
        if command == "1":
            self.change_name()
        elif command == "2":
            self.change_url()
        print()
        self.printer.print_main_commands()
    
    def change_name(self):
        name = input("Which recipe's name do you want to change (return with 'enter')? ")
        if name != "":
            new_name = input("New name (return with 'enter'): ")
            if new_name != "":
                changed = self.recipe_service.change_name(name, new_name)
                if not changed:
                    print(f"There is no recipe called {name}")
                else:
                    print("Name changed")

    def change_url(self):
        name = input("Which recipe's url do you want to change (return with 'enter')? ")
        if name != "":
            url = input("New url (press 'r' to return): ")
            if url != "r":
                changed = self.recipe_service.change_url(name, url)
                if not changed:
                    print(f"There is no recipe called {name}")
                else:
                    print("Url changed")

    def remove_recipe(self):
        name = input("Name of the recipe (return with 'enter'): ")
        if name != "":
            removed = self.recipe_service.remove_recipe(name)
            if not removed:
                print(f"There is no recipe called {name}")
            else:
                print(f"{name} removed")
        print()
        self.printer.print_main_commands()

    def print_recipes(self):
        self.printer.print_printing_options()
        command = input("Command: ")
        if command == "1":
            self.recipe_service.print_all()
        elif command == "2":
            self.print_by_category()
        print()
        self.printer.print_main_commands()        

    def print_by_category(self):
        print("Which category's recipes do you want to print?")
        self.printer.print_categories()
        number = input("Number: ")
        printed = self.recipe_service.print_by_category(number)
        if not printed:
            print("Category doesn't exist")
