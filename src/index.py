from ui.recipe_book import RecipeBook
from initialize_database import initialize_database


initialize_database()
rb = RecipeBook()
rb.start()
