from database_connection import get_database_connection
from entities.recipe import Recipe
# tuleeko oma repositorio tms.?:
from entities.category import Category


class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_recipe(self, recipe):
        cursor = self._connection.cursor()
        same_name = self.find_recipe(recipe.name)
        if not same_name:
            added = cursor.execute(
                "INSERT INTO Recipe (name, url) VALUES (?, ?)",
                (recipe.name, recipe.url))
            return added.lastrowid
        return False

    def remove_recipe(self, name):
        cursor = self._connection.cursor()
        removed = cursor.execute("SELECT name FROM Recipe WHERE name = (?)", [name]).fetchone()
        cursor.execute("DELETE FROM Recipe WHERE name = (?)", [name])
        return removed

    def get_url(self, name):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Recipe WHERE name = (?)", [name])
        recipe = cursor.fetchone()
        return Recipe(recipe["name"], recipe["url"]).url

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Recipe")
        rows = cursor.fetchall()
        return [Recipe(row["name"], row["url"]) for row in rows]

    def find_recipe(self, name):
        cursor = self._connection.cursor()
        recipe = cursor.execute(
            "SELECT * FROM Recipe WHERE name = (?)",
            [name]).fetchone()
        return recipe

    # tuleeko oma repositorio tms.?:
    def add_category(self, category):
        cursor = self._connection.cursor()
        added = cursor.execute(
            "INSERT INTO Category (name) VALUES (?)",
            [category.name])
        return added.lastrowid
    
    def add_recipe_category(self, recipe_id, category_id):
        pass


# testejä
    def get_recipe_id(self, name):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM Recipe WHERE name = (?)', [name])
        recipe = cursor.fetchone()
        return recipe
    
    def find_all_categories(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Category")
        rows = cursor.fetchall()
        return [Category(row["name"]) for row in rows]


recipe_repository = RecipeRepository(get_database_connection())
