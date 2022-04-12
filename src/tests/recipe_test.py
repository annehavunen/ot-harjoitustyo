import unittest
from entities.recipe import Recipe


class TestRecipe(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipe("name", "address")

    def test_name_of_the_recipe(self):
        name = self.recipe.name
        self.assertEqual(name, "name")

    def test_url_of_the_recipe(self):
        url = self.recipe.url
        self.assertEqual(url, "address")
