import webbrowser
from repositories.recipe_repository import RecipeRepository
from entities.recipe import Recipe
from database_connection import get_database_connection
from ui.print_commands import PrintCommands
from entities.category import Category


class RecipeService:
    def __init__(self):
        self.repository = RecipeRepository(get_database_connection())
        self.printer = PrintCommands()

    def add_recipe(self, name, url):
        recipe = Recipe(name, url)
        added = self.repository.add_recipe(recipe)
        if added is False:
            print(f"Recipe with the name {name} exists already.")
        else:
            recipe.add_id(added)
        print()
        return added
    
    def add_categories(self, recipe_id, types):
        added = set()
        for char in types:
            try:
                number = int(char)
                if number in range(1, (self.printer.categories()+1)) and number not in added:
                    category_id = self.add_category(number)
                    self.repository.add_recipe_category(recipe_id, category_id)
                    added.add(number)
            except ValueError:
                pass

    def add_category(self, number):
        name = ""
        if number == 1:
            name = "meat and poultry"
        elif number == 2:
            name = "seafood"
        elif number == 3:
            name = "vegetarian"
        elif number == 4:
            name = "snacks and side dishes"
        elif number == 5:
            name = "desserts"
        elif number == 6:
            name = "baking"
        elif number == 7:
            name = "other"
        
        category = Category(name)
        category_id = self.repository.add_category(category)
        category.add_id(category_id)
        return category_id

    def add_recipe_category(self, recipe_id, category_id):
        self.repository.add_recipe_category(recipe_id, category_id)

    def print_recipes(self):
        self.printer.print_printing_options()
        command = input("Command: ")
        if command == "1":
            recipes = self.repository.find_all()
            for recipe in recipes:
                print(recipe)
            print()
        elif command == "2":
            self.print_by_category()
        else:
            pass
        print()
        self.printer.print_main_commands()

    def open_recipe(self, name):
        exists = self.repository.find_recipe(name)
        if exists is None:
            print(f"There is no recipe called {name}")
        else:
            url = self.repository.get_url(name) # mitä jos on tyhjä?
            webbrowser.open(url)
        print()

    def change_url(self, name, url):
        recipe_id = self.repository.get_recipe_id(name)
        if recipe_id:
            # poista resepti, lisää uudella osoitteella
            # kategorioihin ei kosketa, reseptikategoriat poistetaan ja muutetaan
            category_ids = self.get_category_ids(recipe_id)
            if category_ids:
                pass
            self.repository.remove_recipe(name)
            self.repository.add_recipe(Recipe(name, url))
            print("Url changed")
            print()
            self.printer.print_main_commands()
        else:
            print(f"There is no recipe called {name}")
            print()
            self.printer.print_main_commands()

    def change_name(self, name, new_name):
        recipe = self.repository.find_recipe(name)
        if recipe is None:
            print(f"There is no recipe called {name}")
            print()
            self.printer.print_main_commands()
        else:
            new_url = self.repository.get_url(name)
            self.repository.remove_recipe(name)
            self.repository.add_recipe(Recipe(new_name, new_url))
            print("Name changed")
            print()
            self.printer.print_main_commands()

    def print_all(self):
        recipes = self.repository.find_all()
        for recipe in recipes:
            print(recipe)

    def print_by_category(self, input): # monta kategoriaa?
        try: 
            number = int(input)
            if number in range(1, self.printer.categories()+1):
                name = ""
                if number == 1:
                    name = "meat and poultry"
                elif number == 2:
                    name = "seafood"
                elif number == 3:
                    name = "vegetarian"
                elif number == 4:
                    name = "snacks and side dishes"
                elif number == 5:
                    name = "desserts"
                elif number == 6:
                    name = "baking"
                else:
                    name = "other"
                recipes = self.repository.find_by_category(name)
                for recipe in recipes:
                    print(recipe)
            else:
                print("Category doesn't exist")
                print()
                self.printer.print_main_commands()
        except ValueError:
            print("Category doesn't exist")
            print()
            self.printer.print_main_commands()

    def remove_recipe(self, name):
        recipe_id = self.repository.get_recipe_id(name)
        if recipe_id:
            self.repository.remove_recipe(name)
            category_ids = self.get_category_ids(recipe_id)
            if category_ids:
                for category_id in category_ids:
                    self.remove_category(category_id)
                    self.remove_recipe_category(recipe_id, category_id)
            print(f"{name} removed")
        else:
            print(f"There is no recipe called {name}")
        print()
        self.printer.print_main_commands()
    
    def remove_category(self, category_id):
        self.repository.remove_category(category_id)
    
    def remove_recipe_category(self, recipe_id, category_id):
        self.repository.remove_recipe_category(recipe_id, category_id)

    def get_recipe_id(self, name):
        id = self.repository.get_recipe_id(name)
        return id
    
    def get_category_ids(self, recipe_id):
        category_ids = self.repository.get_category_ids(recipe_id)
        return category_ids
