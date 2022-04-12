import unittest
from repositories.recipe_repository import recipe_repository
from entities.recipe import Recipe


class TestRecipeRepository(unittest.TestCase):
    def setUp(self):
        self.cheesecake = Recipe("cheese cake", "https://www.valio.fi/reseptit/new-york-cheese-cake/")

    def test_add_recipe(self):
        recipe_repository.add_recipe(self.cheesecake)
        recipes = recipe_repository.find_all()

        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0].name, self.cheesecake.name)
        self.assertEqual(recipes[0].url, self.cheesecake.url)
