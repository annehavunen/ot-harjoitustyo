from database_connection import get_database_connection
from entities.recipe import Recipe


class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_recipe(self, recipe):
        cursor = self._connection.cursor()
        same_name = self.find_recipe(recipe.name)
        if not same_name:
            cursor.execute(
                'INSERT INTO Recipes (name, url) VALUES (?, ?)',
                (recipe.name, recipe.url))
            return True
        return False

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

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Recipes")
        rows = cursor.fetchall()
        return [Recipe(row["name"], row["url"]) for row in rows]

    def find_recipe(self, name):
        cursor = self._connection.cursor()
        recipe = cursor.execute(
            'SELECT * FROM Recipes WHERE name = (?)',
            [name]).fetchone()
        return recipe

recipe_repository = RecipeRepository(get_database_connection())
