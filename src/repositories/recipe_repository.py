#from database_connection import get_database_connection
from entities.recipe import Recipe

class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection
        self.recipe_list = []

    def add_recipe(self, recipe):
#        self.recipe_list.append(recipe)
#        def create(self, user):

        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO Recipes (name, url) VALUES (?, ?)', (recipe.name, recipe.url))

    def get_recipes(self):
        return self.recipe_list

    def remove_recipe(self, name):
        cursor = self._connection.cursor()
        removed = cursor.execute('SELECT name FROM Recipes WHERE name = (?)', [name]).fetchone()
#        if removed == None:
#            print("There is no")
        cursor.execute('DELETE FROM Recipes WHERE name = (?)', [name])
        #self.recipe_list.remove(recipe)
        return removed

    def get_url(self, name):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM Recipes WHERE name = (?)', [name])
        recipe = cursor.fetchone()
        return Recipe(recipe["name"], recipe["url"]).url
        #print([Recipe(row["name"], row["name"]) for row in recipe])
        #return url

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
#        return [Recipe(row["id"], row["name"]) for row in rows]

#user_repository = RecipeRepository(get_database_connection())
#users = user_repository.find_all()
