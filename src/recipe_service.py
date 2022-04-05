from recipe_repository import RecipeRepository
from recipe import Recipe

class RecipeService:
    def __init__(self):
        self.repository = RecipeRepository()

    def add_recipe(self, name):
        recipe = Recipe(name)
        self.repository.add_recipe(recipe)
        print()

    def print_recipes(self):
        recipes = self.repository.get_recipes()
        print("List of all recipes:")
        for r in recipes:
            print(r)
        print()
    
    def remove_recipe(self, name):
        recipes = self.repository.get_recipes()
        doesnt_exist = True
        for recipe in recipes:
            if recipe.name == name:
                self.repository.remove_recipe(recipe)
                doesnt_exist = False
                print(f"{name} removed")
        if doesnt_exist:
            print(f"There is no recipe called {name}")
        print()
        
