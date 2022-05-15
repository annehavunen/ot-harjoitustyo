import webbrowser
from entities.recipe import Recipe
from entities.category import Category
from ui.print_commands import PrintCommands
from repositories.recipe_repository import (
    recipe_repository as default_recipe_repository
)

class RecipeService:
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(self, recipe_repository=default_recipe_repository):
        """Luokan konstruktori. Luo sovelluslogiikasta vastaavan palvelun.

        Args:
            repository:
                Oletusarvoltaan RecipeRepository-olio.
                Olio, jolla on RecipeRepository-luokkaa vastaavat metodit.
            printer:
                Oletusarvoltaan PrintCommands-olio.
                Olio, jolla on PrintCommands-luokkaa vastaavat metodit.
        """
        self._repository = recipe_repository
        self._printer = PrintCommands()

    def add_recipe(self, name, url, directions):
        """Luo uuden reseptin.

        Args:
            name: Merkkijonoarvo, joka kuvaa reseptin nimeä.
            url: Merkkijonoarvo, joka kuvaa reseptin verkko-osoitetta.

        Returns:
            Luodun reseptin id, mikäli lisäys onnistui. Muussa tapauksessa None.
        """
        recipe_id = self._repository.get_recipe_id(name)
        if not recipe_id:
            recipe = Recipe(name, url, directions)
            recipe_id = self._repository.add_recipe(recipe)
            return recipe_id
        return None

    def add_categories(self, recipe_id, types):
        """Lisää kategoriat ja resepti-kategoriat yksi kerrallaan.

        Args:
            recipe_id: Integer-arvo, joka kuvaa reseptin id-tunnusta.
            types: Merkkijonoarvo, joka kuvaa lisättäviä kategorioita.
        """
        added = set()
        for char in types:
            try:
                number = int(char)
                if number in range(1, (self._printer.categories()+1)) and number not in added:
                    category_id = self.add_category(number)
                    self._repository.add_recipe_category(recipe_id, category_id)
                    added.add(number)
            except ValueError:
                pass

    def add_category(self, number):
        """Luo uuden kategorian.

        Args:
            number: Integer-arvo, joka kuvaa kategorian numeroa.

        Returns:
            Luodun kategorian id.
        """
        name = ""
        if number == 1:
            name = "meat and poultry"
        elif number == 2:
            name = "seafood"
        elif number == 3:
            name = "vegetarian"
        elif number == 4:
            name = "snacks and side dishes"
        elif number == 5:
            name = "desserts"
        elif number == 6:
            name = "baking"
        else:
            name = "other"
        category = Category(name)
        category_id = self._repository.add_category(category)
        return category_id

    def add_recipe_category(self, recipe_id, category_id):
        """Luo uuden resepti-kategorian.

        Args:
            recipe_id: Integer-arvo, joka kuvaa reseptin id-tunnusta.
            category_id: Integer-arvo, joka kuvaa kategorian id-tunnusta.
        """
        self._repository.add_recipe_category(recipe_id, category_id)

    def open_recipe(self, name):
        """Avaa valitun reseptin verkkosivun.

        Args:
            name: Merkkijonoarvo, joka kuvaa reseptin nimeä.
        """
        url = self._repository.get_recipe_url(name)
        webbrowser.open(url)

    def change_url(self, name, new_url):
        """Muuttaa reseptin URL-osoitetta.

        Args:
            name: Merkkijonoarvo, joka kuvaa reseptin nimeä.
            new_url: Merkkijonoarvo, joka kuvaa reseptin uutta URL-osoitetta.
        """
        recipe_id = self._repository.get_recipe_id(name)
        self._repository.change_url(new_url, recipe_id)

    def change_name(self, recipe_id, new_name):
        """Muuttaa reseptin nimeä.

        Args:
            name: Merkkijonoarvo, joka kuvaa reseptin nimeä.
            new_name: Merkkijonoarvo, joka kuvaa reseptin uutta nimeä.
        """
        self._repository.change_name(recipe_id, new_name)

    def change_directions(self, name, new_directions):
        """Muuttaa reseptin ohjetta.

        Args:
            name: Merkkijonoarvo, joka kuvaa reseptin nimeä.
            new_directions: Merkkijonoarvo, joka kuvaa reseptin uutta ohjetta.
        """
        self._repository.change_directions(name, new_directions)

    def list_by_category(self, name):
        """Palauttaa valitun kategorian reseptit.

        Args:
            name: Merkkijonoarvo, joka kuvaa kategorian nimeä.

        Returns:
            Reseptien nimet listana.
        """
        if name == "show all":
            recipes = self.list_all()
        else:
            recipes = self._repository.list_by_category(name)
        return recipes

    def list_all(self):
        """Palauttaa kaikki reseptit.

        Returns:
            Reseptien nimet listana.
        """
        recipes = self._repository.list_all()
        return recipes

    def remove_recipe(self, name):
        """Poistaa reseptin sekä siihen liittyvät kategoriat.

        Args:
            name: Merkkijonoarvo, joka kuvaa reseptin nimeä.
        """
        recipe_id = self._repository.get_recipe_id(name)
        self._repository.remove_recipe(name)
        category_ids = self.get_category_ids(recipe_id)
        if category_ids:
            for category_id in category_ids:
                self.remove_category(category_id)
                self.remove_recipe_category(recipe_id, category_id)

    def remove_category(self, category_id):
        """Poistaa kategorian.

        Args:
            category_id: Integer-arvo, joka kuvaa kategorian id-tunnusta.
        """
        self._repository.remove_category(category_id)

    def remove_recipe_category(self, recipe_id, category_id):
        """Poistaa resepti-kategorian.

        Args:
            recipe_id: Integer-arvo, joka kuvaa reseptin id-tunnusta.
            category_id: Integer-arvo, joka kuvaa kategorian id-tunnusta.
        """
        self._repository.remove_recipe_category(recipe_id, category_id)

    def get_recipe_id(self, name):
        """Palauttaa reseptin id-tunnuksen.

        Args:
            name: Merkkijonoarvo, joka kuvaa reseptin nimeä.

        Returns:
            Reseptin id-tunnus Integer-arvona.
        """
        recipe_id = self._repository.get_recipe_id(name)
        return recipe_id

    def get_category_ids(self, recipe_id):
        """Palauttaa reseptiin liittyvät kategoriat.

        Args:
            recipe_id: Integer-arvo, joka kuvaa reseptin id-tunnusta.

        Returns:
            Kategorioiden numerot listana.
        """
        category_ids = self._repository.get_category_ids(recipe_id)
        return category_ids

    def get_categories(self):
        return self._repository.get_categories()

    def get_recipe_categories(self):
        return self._repository.get_recipe_categories()

    def get_url(self, name):
        return self._repository.get_recipe_url(name)

    def get_recipe_name(self, recipe_id):
        return self._repository.get_recipe_name(recipe_id)

    def get_recipe_directions(self, name):
        return self._repository.get_recipe_directions(name)

recipe_service = RecipeService()
