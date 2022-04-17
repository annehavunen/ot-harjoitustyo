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
        if not added:
            print(f"Recipe with the name {name} exists already.")
        else:
            print("Recipe added")
        print()

    def print_recipes(self):
        recipes = self.repository.find_all()
        for recipe in recipes:
            print(recipe)
        print()

    def open_recipe(self, name):
        exists = self.repository.find_recipe(name)
        if exists is None:
            print(f"There is no recipe called {name}")
        else:
            url = self.repository.get_url(name)
            webbrowser.open(url)
        print()

    def change_url(self, name, url):
        recipe = self.repository.find_recipe(name)
        if recipe is None:
            print(f"There is no recipe called {name}")
            print()
            self.printer.print_main_commands()
        else:
            self.repository.remove_recipe(name)
            self.repository.add_recipe(Recipe(name, url))
            print("Url changed")
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

    def remove_recipe(self, name):
        removed = self.repository.remove_recipe(name)
        if removed is None:
            print(f"There is no recipe called {name}")
        else:
            print(f"{name} removed")
        print()
    
    def add_category(self, type):
        category = Category(type)
        self.repository.add_category(category)
        print()
    
    def print_categories(self):
        categories = self.repository.find_all_categories()
        for category in categories:
            print(category) # tarvitaanko tulostustoiminto
        print()
