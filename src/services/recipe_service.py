import webbrowser
from repositories.recipe_repository import RecipeRepository
from entities.recipe import Recipe
from entities.category import Category
from database_connection import get_database_connection
from ui.print_commands import PrintCommands


class RecipeService:
    def __init__(self):
        self.repository = RecipeRepository(get_database_connection())
        self.printer = PrintCommands()

    def add_recipe(self, name, url):
        recipe_id = self.repository.get_recipe_id(name)
        if not recipe_id:
            recipe = Recipe(name, url)
            recipe_id = self.repository.add_recipe(recipe)
            return recipe_id
        return False

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
        return category_id

    def add_recipe_category(self, recipe_id, category_id):
        self.repository.add_recipe_category(recipe_id, category_id)

    def open_recipe(self, name):
        url = self.repository.get_url(name)
        webbrowser.open(url)

    def change_url(self, name, new_url):
        recipe_id = self.repository.get_recipe_id(name)
        if recipe_id:
            self.repository.change_url(new_url, recipe_id)
            return True
        return False

    def change_name(self, name, new_name):
        recipe_id = self.repository.get_recipe_id(name)
        if recipe_id:
            self.repository.change_name(new_name, recipe_id)
            return True
        return False

    def print_all(self): # tekstikäyttöliittymä, poistan myöhemmin
        recipes = self.repository.find_all()
        for recipe in recipes:
            print(recipe)

    def print_by_category(self, name):  # tekstikäyttöliittymä, poistan myöhemmin
        recipes = self.repository.find_by_category(name)
        for recipe in recipes:
            print(recipe)

    def list_by_category(self, name):
        # if number==0, haetaan kaikki
        # recipes = []
#        recipe_names = []
        if name == "show all":
            recipes = self.repository.list_all()
        else:
            recipes = self.repository.list_by_category(name)
        return recipes
#        print(recipe_names)


    def remove_recipe(self, name):
        recipe_id = self.repository.get_recipe_id(name)
        if recipe_id:
            self.repository.remove_recipe(name)
            category_ids = self.get_category_ids(recipe_id)
            if category_ids:
                for category_id in category_ids:
                    self.remove_category(category_id)
                    self.remove_recipe_category(recipe_id, category_id)
            return True
        return False

    def remove_category(self, category_id):
        self.repository.remove_category(category_id)

    def remove_recipe_category(self, recipe_id, category_id):
        self.repository.remove_recipe_category(recipe_id, category_id)

    def get_recipe_id(self, name):
        recipe_id = self.repository.get_recipe_id(name)
        return recipe_id

    def get_category_ids(self, recipe_id):
        category_ids = self.repository.get_category_ids(recipe_id)
        return category_ids

    def get_categories(self):
        return self.repository.get_categories()

    def get_recipe_categories(self):
        return self.repository.get_recipe_categories()

    def get_url(self, name):
        return self.repository.get_url(name)

    def get_recipe_name(self, recipe_id):
        return self.repository.get_recipe_name(recipe_id)

# testi
# recipe_service = RecipeService()