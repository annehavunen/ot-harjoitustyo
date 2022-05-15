from database_connection import get_database_connection
from entities.recipe import Recipe


class RecipeRepository:
    """Resepteihin ja kategorioihin liittyvistä tietokantaoperaatioista vastaava luokka"""

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden connect-olio.
        """
        self._connection = connection

    def add_recipe(self, recipe):
        """Tallentaa reseptin tietokantaan.

        Args:
            recipe: Tallennettava resepti Recipe-oliona.

        Returns:
            Tallennetun reseptin id-tunnus.
        """
        cursor = self._connection.cursor()
        added = cursor.execute(
            "INSERT INTO Recipe (name, url, directions) VALUES (?, ?, ?)",
            (recipe.name, recipe.url, recipe.directions))
        return added.lastrowid

    def add_category(self, category):
        """Tallentaa kategorian tietokantaan.

        Args:
            category: Tallennettava kategoria Category-oliona.

        Returns:
            Tallennetun reseptin id-tunnus.
        """
        cursor = self._connection.cursor()
        added = cursor.execute(
            "INSERT INTO Category (name) VALUES (?)",
            [category.name])
        return added.lastrowid

    def add_recipe_category(self, recipe_id, category_id):
        """Tallentaa resepti-kategorian tietokantaan.

        Args:
            recipe_id: Integer-arvo, joka kuvaa tallennettavan reseptin id-tunnusta.
            category_id: Integer-arvo, joka kuvaa tallennettavan kategorian id-tunnusta.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO Recipe_category VALUES (?, ?)",
            (recipe_id, category_id))

    def list_all(self):
        """Palauttaa kaikki reseptit.

        Returns:
            Reseptien nimet listana.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT name FROM Recipe")
        rows = cursor.fetchall()
        return [row[0] for row in rows]

    def list_by_category(self, name):
        """Palauttaa valitun kategorian reseptit.

        Args:
            name: Merkkijonoarvo, joka kuvaa kategorian nimeä.

        Returns:
            Reseptien nimet listana.
        """
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT R.name FROM Recipe R, Category C, Recipe_category RC
            WHERE C.name = (?) AND R.id = RC.recipe_id AND C.id = RC.category_id""",
            [name])
        rows = cursor.fetchall()
        return [row[0] for row in rows]

    def get_recipe_url(self, name):
        """Palauttaa URL-osoitteen nimen perusteella.

        Args:
            name: Merkkijonoarvo, joka kuvaa reseptin nimeä.

        Returns:
            Reseptin URL-osoite merkkijonoarvona.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Recipe WHERE name = (?)", [name])
        recipe = cursor.fetchone()
        return recipe[2]

    def get_recipe_id(self, name):
        """Palauttaa reseptin id-tunnuksen nimen perusteella.

        Args:
            name: Merkkijonoarvo, joka kuvaa reseptin nimeä.

        Returns:
            Reseptin id-tunnus Integer-arvona, jos resepti löytyy. Muussa tapauksessa None.
        """
        cursor = self._connection.cursor()
        recipe = cursor.execute(
            "SELECT id FROM Recipe WHERE name = (?)",
            [name]).fetchone()
        if recipe:
            return recipe[0]
        return None

    def get_category_ids(self, recipe_id):
        """Palauttaa reseptiin liittyvät kategoriat.

        Args:
            recipe_id: Integer-arvo, joka kuvaa reseptin id-tunnusta.

        Returns:
            Kategorioiden numerot listana, jos kategorioita löytyy. Muussa tapauksessa None.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT category_id FROM Recipe_category WHERE recipe_id = (?)",
            [recipe_id]
        )
        rows = cursor.fetchall()
        if rows:
            return [row[0] for row in rows]
        return None

    def remove_recipe(self, name):
        """Poistaa reseptin.

        Args:
            name: Merkkijonoarvo, joka kuvaa reseptin nimeä.

        Returns:
            Reseptin id-tunnus Integer-arvona.
        """
        cursor = self._connection.cursor()
        recipe = cursor.execute("SELECT * FROM Recipe WHERE name = (?)", [name]).fetchone()
        recipe_id = recipe[0]
        cursor.execute("DELETE FROM Recipe WHERE name = (?)", [name])
        return recipe_id

    def remove_category(self, category_id):
        """Poistaa kategorian.

        Args:
            category_id: Integer-arvo, joka kuvaa reseptin id-tunnusta.
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Category WHERE id = (?)", [category_id])

    def remove_recipe_category(self, recipe_id, category_id):
        """Poistaa resepti-kategorian.

        Args:
            recipe_id: Integer-arvo, joka kuvaa reseptin id-tunnusta.
            category_id: Integer-arvo, joka kuvaa kategorian id-tunnusta.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "DELETE FROM Recipe_category WHERE recipe_id = (?) and category_id = (?)",
            (recipe_id, category_id))

    def change_url(self, new_url, recipe_id):
        """Muuttaa reseptin URL-osoitetta.

        Args:
            new_url: Merkkijonoarvo, joka kuvaa reseptin uutta URL-osoitetta.
            recipe_id: Integer-arvo, joka kuvaa reseptin id-tunnusta.
        """
        cursor = self._connection.cursor()
        cursor.execute("UPDATE Recipe SET url = (?) WHERE id = (?)", (new_url, recipe_id))

    def change_name(self, recipe_id, new_name):
        """Muuttaa reseptin nimeä.

        Args:
            recipe_id: Integer-arvo, joka kuvaa reseptin id-tunnusta.
            new_name: Merkkijonoarvo, joka kuvaa reseptin uutta nimeä.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE Recipe SET name = (?) WHERE id = (?)", (new_name, recipe_id))

    def change_directions(self, name, new_directions):
        """Muuttaa reseptin ohjetta.

        Args:
            name: Merkkijonoarvo, joka kuvaa reseptin nimeä.
            new_directions: Merkkijonoarvo, joka kuvaa reseptin uutta ohjetta.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE Recipe SET directions = (?) WHERE name = (?)", (new_directions, name))

    def find_all(self):
        """Palauttaa kaikki reseptit.

        Returns:
            Lista Recipe-olioita.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Recipe")
        rows = cursor.fetchall()
        return [Recipe(row["name"], row["url"], row["directions"]) for row in rows]

    def get_categories(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Category")
        rows = cursor.fetchall()
        return [(row[0], row[1]) for row in rows]

    def get_recipe_categories(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Recipe_category")
        rows = cursor.fetchall()
        return [(row[0], row[1]) for row in rows]

    def get_recipe_name(self, recipe_id):
        cursor = self._connection.cursor()
        recipe = cursor.execute("SELECT name FROM Recipe WHERE id = (?)", [recipe_id]).fetchone()
        return recipe[0]

    def get_recipe_directions(self, name):
        cursor = self._connection.cursor()
        recipe = cursor.execute("SELECT directions FROM Recipe WHERE name = (?)", [name]).fetchone()
        return recipe[0]

recipe_repository = RecipeRepository(get_database_connection())
