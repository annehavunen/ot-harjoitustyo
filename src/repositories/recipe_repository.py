from database_connection import get_database_connection
from entities.recipe import Recipe
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

    def find_recipe(self, name):    # poista myöhemmin?
        cursor = self._connection.cursor()
        recipe = cursor.execute(
            "SELECT * FROM Recipe WHERE name = (?)",
            [name]).fetchone()
        return recipe

    def add_category(self, category):
        cursor = self._connection.cursor()
        added = cursor.execute(
            "INSERT INTO Category (name) VALUES (?)",
            [category.name])
        return added.lastrowid
    
    def add_recipe_category(self, recipe_id, category_id):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO Recipe_category VALUES (?, ?)",
            (recipe_id, category_id))

    def find_by_category(self, name):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT R.name, R.url FROM Recipe R, Category C, Recipe_category RC WHERE C.name = (?) AND R.id = RC.recipe_id AND C.id = RC.category_id",
            [name])
        rows = cursor.fetchall()
        return [Recipe(row["name"], row["url"]) for row in rows]
    
    def get_recipe_id(self, name):
        cursor = self._connection.cursor()
        recipe = cursor.execute(
            "SELECT id FROM Recipe WHERE name = (?)",
            [name]).fetchone()
        try:
            return recipe[0]
        except:
            return None
    
    def get_category_ids(self, recipe_id):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT category_id FROM Recipe_category WHERE recipe_id = (?)",
            [recipe_id]
        )
        rows = cursor.fetchall()
        if rows:
            return [row[0] for row in rows]
        else:
            return None

    def remove_recipe(self, name):
        cursor = self._connection.cursor()
        recipe = cursor.execute("SELECT * FROM Recipe WHERE name = (?)", [name]).fetchone()
        recipe_id = recipe[0]
        cursor.execute("DELETE FROM Recipe WHERE name = (?)", [name])
        return recipe_id

    def remove_category(self, category_id):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Category WHERE id = (?)", [category_id])

    def remove_recipe_category(self, recipe_id, category_id):
        cursor = self._connection.cursor()
        cursor.execute(
            "DELETE FROM Recipe_category WHERE recipe_id = (?) and category_id = (?)",
            (recipe_id, category_id))

recipe_repository = RecipeRepository(get_database_connection())
