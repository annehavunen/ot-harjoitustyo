import unittest
from repositories.recipe_repository import recipe_repository
from entities.recipe import Recipe
from entities.category import Category
import initialize_database


class TestRecipeRepository(unittest.TestCase):
    def setUp(self):
        self.cheesecake = Recipe("cheese cake", "https://www.valio.fi/reseptit/new-york-cheese-cake/")
        self.category = Category("baking")
        initialize_database.initialize_database()

    def test_add_recipe(self):
        recipe_repository.add_recipe(self.cheesecake)
        recipes = recipe_repository.find_all()
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0].name, self.cheesecake.name)
        self.assertEqual(recipes[0].url, self.cheesecake.url)

        dublicate = Recipe("cheese cake", "https://www.arla.fi/reseptit/new-york-cheesecake/")
        recipe_repository.add_recipe(dublicate)
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0].url, self.cheesecake.url)

    def test_get_url(self):
        recipe_repository.add_recipe(self.cheesecake)
        url = recipe_repository.get_url(self.cheesecake.name)
        self.assertEqual(url, self.cheesecake.url)

    def test_add_category(self):
        recipe_repository.add_category(self.category)
        categories = recipe_repository.get_categories()
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0][0], 1)
        self.assertEqual(categories[0][1], "baking")

    def test_add_recipe_category(self):
        recipe_repository.add_recipe_category(1, 2)
        categories = recipe_repository.get_recipe_categories()
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0][0], 1)
        self.assertEqual(categories[0][1], 2)

    def test_remove_recipe(self):
        recipe_repository.add_recipe(self.cheesecake)
        recipe_repository.remove_recipe(self.cheesecake.name)
        recipes = recipe_repository.find_all()
        self.assertEqual(len(recipes), 0)

    def test_remove_category(self):
        category_id = recipe_repository.add_category(self.category)
        recipe_repository.remove_category(category_id)
        categories = recipe_repository.get_categories()
        print(categories)
        self.assertEqual(len(categories), 0)

    def test_remove_recipe_category(self):
        recipe_repository.add_recipe_category(1, 1)
        recipe_repository.remove_recipe_category(1, 1)
        recipe_categories = recipe_repository.get_recipe_categories()
        self.assertEqual(len(recipe_categories), 0)
