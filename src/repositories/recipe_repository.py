from database_connection import get_database_connection
from entities.recipe import Recipe


class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_recipe(self, recipe):
        cursor = self._connection.cursor()
        same_name = cursor.execute('SELECT name FROM Recipes WHERE name = (?)', [recipe.name]).fetchone()
        if not same_name:
            cursor.execute('INSERT INTO Recipes (name, url) VALUES (?, ?)', (recipe.name, recipe.url))
            return True
        return False

    def get_recipes(self):
        return self.recipe_list

    def remove_recipe(self, name):
        cursor = self._connection.cursor()
        removed = cursor.execute('SELECT name FROM Recipes WHERE name = (?)', [name]).fetchone()
        cursor.execute('DELETE FROM Recipes WHERE name = (?)', [name])
        return removed

    def get_url(self, name):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM Recipes WHERE name = (?)', [name])
        recipe = cursor.fetchone()
        return Recipe(recipe["name"], recipe["url"]).url

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < len(self.recipe_list):
            recipe = self.recipe_list[self.iterator]
            self.iterator += 1
            return recipe
        raise StopIteration

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Recipes")
        rows = cursor.fetchall()
        return [Recipe(row["name"], row["url"]) for row in rows]

recipe_repository = RecipeRepository(get_database_connection())
