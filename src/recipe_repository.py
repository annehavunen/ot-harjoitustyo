"""Contains only names of the recipes in a list for now.
"""

class RecipeRepository:
    def __init__(self):
        self.recipe_list = []
    
    def add_recipe(self, recipe):
        self.recipe_list.append(recipe)

    def get_recipes(self):
        return self.recipe_list

    def remove_recipe(self, recipe):
        self.recipe_list.remove(recipe)
    
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.recipe_list):
            recipe = self.recipe_list[self.n]
            self.n += 1
            return recipe
        else:
            raise StopIteration
