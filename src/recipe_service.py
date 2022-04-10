from repositories.recipe_repository import RecipeRepository
from entities.recipe import Recipe
from database_connection import get_database_connection
import webbrowser


class RecipeService:
    def __init__(self):
        self.repository = RecipeRepository(get_database_connection())

    def add_recipe(self, name, url):
        recipe = Recipe(name, url)
        self.repository.add_recipe(recipe)
        print()

    def print_recipes(self):
        recipes = self.repository.find_all()
        # print(recipes)
        # recipes = self.repository.get_recipes()
        # print("List of all recipes:")
        for recipe in recipes:
            print(recipe)
        print()

    def remove_recipe(self, name):
        removed = self.repository.remove_recipe(name)
        if removed == None:
            print(f"There is no recipe called {name}")
        else:
            print(f"{name} removed")
        # recipes = self.repository.get_recipes()
        # doesnt_exist = True
        # for recipe in recipes:
        #     if recipe.name == name:
        #         self.repository.remove_recipe(recipe)
        #         doesnt_exist = False
        #         print(f"{name} removed")
        # if doesnt_exist:
        #     print(f"There is no recipe called {name}")
        print()

    def open_recipe(self, title):
        url = self.repository.get_url(title)
        #print(url)
        webbrowser.open(url)
        print()
