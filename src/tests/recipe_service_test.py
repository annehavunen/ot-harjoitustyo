import unittest
from services.recipe_service import RecipeService
from repositories.recipe_repository import recipe_repository
from entities.recipe import Recipe
import initialize_database


class TestRecipeService(unittest.TestCase):
    def setUp(self):
        self.service = RecipeService()
        self.cheesecake = Recipe("cheese cake", "https://www.valio.fi/reseptit/new-york-cheese-cake/", "")
        initialize_database.initialize_database()

    def test_add_recipe(self):
        self.service.add_recipe(self.cheesecake.name, self.cheesecake.url, self.cheesecake.directions)
        recipes = recipe_repository.find_all()
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0].name, self.cheesecake.name)
        self.assertEqual(recipes[0].url, self.cheesecake.url)
        recipe_id = self.service.add_recipe(self.cheesecake.name, self.cheesecake.url, self.cheesecake.directions)
        self.assertEqual(None, recipe_id)

    def test_add_categories(self):
        recipe_id = self.service.add_recipe(self.cheesecake.name, self.cheesecake.url, self.cheesecake.directions)
        self.service.add_categories(recipe_id, "112345678A")
        categories = self.service.get_categories()
        self.assertEqual(len(categories), 7)

    def test_add_category(self):
        self.service.add_category(1)
        categories = self.service.get_categories()
        self.assertEqual(len(categories), 1)

    def test_add_recipe_category(self):
        self.service.add_recipe_category(1, 1)
        recipe_categories = self.service.get_recipe_categories()
        self.assertEqual(len(recipe_categories), 1)

    def test_change_url(self):
        self.service.add_recipe(self.cheesecake.name, self.cheesecake.url, self.cheesecake.directions)
        self.service.change_url(self.cheesecake.name, "new.address")
        url = self.service.get_url(self.cheesecake.name)
        self.assertEqual(url, "new.address")

    def test_change_name(self):
        self.service.add_recipe(self.cheesecake.name, self.cheesecake.url, self.cheesecake.directions)
        recipe_id = self.service.get_recipe_id(self.cheesecake.name)
        self.service.change_name(recipe_id, "new name")
        name = self.service.get_recipe_name(recipe_id)
        self.assertEqual(name, "new name")
    
    def test_list_by_category(self):
        recipe_id = self.service.add_recipe(self.cheesecake.name, self.cheesecake.url, self.cheesecake.directions)
        self.service.add_categories(recipe_id, "6")
        recipes = self.service.list_by_category("baking")
        self.assertEqual(len(recipes), 1)
        recipes = self.service.list_by_category("show all")
        self.assertEqual(len(recipes), 1)
    
    def test_list_all(self):
        self.service.add_recipe(self.cheesecake.name, self.cheesecake.url, self.cheesecake.directions)
        recipes = self.service.list_all()
        self.assertEqual(len(recipes), 1)

    def test_remove_recipe(self):
        recipe_id = self.service.add_recipe(self.cheesecake.name, self.cheesecake.url, self.cheesecake.directions)
        self.service.add_categories(recipe_id, "6")
        self.service.remove_recipe(self.cheesecake.name)
        recipes = recipe_repository.find_all()
        self.assertEqual(len(recipes), 0)
        categories = self.service.get_categories()
        self.assertEqual(len(categories), 0)
    
    def test_remove_category(self):
        category_id = self.service.add_category(1)
        self.service.remove_category(category_id)
        categories = self.service.get_categories()
        self.assertEqual(len(categories), 0)

    def test_remove_recipe_category(self):
        recipe_id = self.service.add_recipe(self.cheesecake.name, self.cheesecake.url, self.cheesecake.directions)
        self.service.add_categories(recipe_id, "6")
        category_ids = self.service.get_category_ids(recipe_id)
        self.service.remove_recipe_category(recipe_id, category_ids[0])
        recipe_categories = self.service.get_recipe_categories()
        self.assertEqual(len(recipe_categories), 0)
