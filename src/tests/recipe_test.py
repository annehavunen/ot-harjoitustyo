import unittest
from entities.recipe import Recipe


class TestRecipe(unittest.TestCase):
    def setUp(self):
        self.r = Recipe("name")

    def test_name_of_the_recipe(self):
        name = self.r.name
        self.assertEqual(name, "name")
