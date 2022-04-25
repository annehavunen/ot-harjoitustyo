import unittest
from services.recipe_service import RecipeService
from repositories.recipe_repository import recipe_repository
from entities.recipe import Recipe
import initialize_database


class TestRecipeService(unittest.TestCase):
    def setUp(self):
        self.service = RecipeService()
        self.cheesecake = Recipe("cheese cake", "https://www.valio.fi/reseptit/new-york-cheese-cake/")
        initialize_database.initialize_database()

    def test_add_recipe(self):
        self.service.add_recipe(self.cheesecake.name, self.cheesecake.url)
        recipes = recipe_repository.find_all()
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0].name, self.cheesecake.name)
        self.assertEqual(recipes[0].url, self.cheesecake.url)

    def test_add_category(self):
        self.service.add_category(1)
        categories = self.service.get_categories()
        self.assertEqual(len(categories), 1)

    def test_add_recipe_category(self):
        self.service.add_recipe_category(1, 1)
        recipe_categories = self.service.get_recipe_categories()
        self.assertEqual(len(recipe_categories), 1)

    def test_change_url(self):
        self.service.add_recipe(self.cheesecake.name, self.cheesecake.url)
        self.service.change_url(self.cheesecake.name, "test.address")
        url = self.service.get_url(self.cheesecake.name)
        self.assertEqual(url, "test.address")

    def test_change_name(self):
        self.service.add_recipe(self.cheesecake.name, self.cheesecake.url)
        recipe_id = self.service.get_recipe_id(self.cheesecake.name)
        self.service.change_name(self.cheesecake.name, "test")
        name = self.service.get_recipe_name(recipe_id)
        self.assertEqual(name, "test")

    def test_remove_recipe(self):
        self.service.add_recipe(self.cheesecake.name, self.cheesecake.url)
        self.service.remove_recipe(self.cheesecake.name)
        recipes = recipe_repository.find_all()
        self.assertEqual(len(recipes), 0)
        exist = self.service.remove_recipe(self.cheesecake.name)
        self.assertEqual(exist, False)
    
    def test_remove_category(self):
        category_id = self.service.add_category(1)
        self.service.remove_category(category_id)
        categories = self.service.get_categories()
        self.assertEqual(len(categories), 0)
