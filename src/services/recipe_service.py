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
        print()
        return added
    
    def add_categories(self, recipe_id, types):
        added = set()
        for char in types:
            try:
                number = int(char)
                if number in range(1, (self.printer.categories()+1)) and number not in added:
                    category_id = self.add_category(number)
                    self.repository.add_recipe_category(recipe_id, category_id)# add_recipe_category(recipe_id, category_id)
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
        return category_id

    def add_recipe_category(self, recipe_id, category_id):
        self.repository.add_recipe_category(recipe_id, category_id)
        # voiko kategorian myöhemmin poistaa category_id:n perusteella recipe_categoryn kautta?

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

    def print_by_category(self, input):
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
        except ValueError:
            print("Category doesn't exist")

    def remove_recipe(self, name):
        removed = self.repository.remove_recipe(name)
        if removed is None:
            print(f"There is no recipe called {name}")
        else:
            print(f"{name} removed")
        print()

    # def add_category(self, type):
    #     category = Category(type)
    #     self.repository.add_category(category)
    #     print()
    
    def print_categories(self):
        categories = self.repository.find_all_categories()
        for category in categories:
            print(category)
        print()

    def print_recipe_id(self, name):
        id = self.repository.get_recipe_id(name)
        print(id)