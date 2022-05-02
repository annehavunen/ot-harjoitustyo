from ui.change_recipe_view import ChangeRecipeView
from ui.main_view import MainView
from ui.add_recipe_view import AddRecipeView
from ui.browse_recipes_view import BrowseRecipesView


class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None
    
    def start(self):
        self.show_main_view()

    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = None

    def show_main_view(self):
        self.hide_current_view()
        self.current_view = MainView(
            self.root,
            self.show_add_recipe_view,
            self.show_browse_recipes_view,
            self.show_change_recipe_view)
        self.current_view.pack()
    
    def show_add_recipe_view(self):
        self.hide_current_view()

        self.current_view = AddRecipeView(
            self.root,
            self.show_main_view
        )
        self.current_view.pack()

    def show_browse_recipes_view(self):
        self.hide_current_view()

        self.current_view = BrowseRecipesView(
            self.root,
            self.show_main_view
        )
        self.current_view.pack()

    def show_change_recipe_view(self):
        self.hide_current_view()

        self.current_view = ChangeRecipeView(
            self.root,
            self.show_main_view
        )
        self.current_view.pack()
