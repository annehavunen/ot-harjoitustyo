from repositories.recipe_repository import RecipeRepository
from entities.recipe import Recipe
from database_connection import get_database_connection
import webbrowser


class RecipeService:
    def __init__(self):
        self.repository = RecipeRepository(get_database_connection())

    def add_recipe(self, name, url):
        recipe = Recipe(name, url)
        added = self.repository.add_recipe(recipe)
        if not added:
            print(f"Recipe with the name {name} exists already.")
        print()

    def print_recipes(self):
        recipes = self.repository.find_all()
        for recipe in recipes:
            print(recipe)
        print()

    def remove_recipe(self, name):
        removed = self.repository.remove_recipe(name)
        if removed == None:
            print(f"There is no recipe called {name}")
        else:
            print(f"{name} removed")
        print()

    def open_recipe(self, title):
        url = self.repository.get_url(title)
        webbrowser.open(url)
        print()
