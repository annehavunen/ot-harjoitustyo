from ui.change_recipe_view import ChangeRecipeView
from ui.change_web_recipe_view import ChangeWebRecipeView
from ui.change_written_recipe_view import ChangeWrittenRecipeView
from ui.main_view import MainView
from ui.add_recipe_view import AddRecipeView
from ui.browse_recipes_view import BrowseRecipesView


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan.

        Args:
            root: TKinter-elementti, jonka sisään käyttöliittymä alustetaan.
        """

        self._root = root
        self._current_view = None


    def start(self):
        """Käynnistää käyttöliittymän"""

        self._show_main_view()


    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None


    def _show_main_view(self):
        self._hide_current_view()
        self._current_view = MainView(
            self._root,
            self._show_add_recipe_view,
            self._show_browse_recipes_view,
            self._show_change_recipe_view)
        self._current_view.pack()
    

    def _show_add_recipe_view(self):
        self._hide_current_view()

        self._current_view = AddRecipeView(
            self._root,
            self._show_main_view
        )
        self._current_view.pack()


    def _show_browse_recipes_view(self):
        self._hide_current_view()

        self._current_view = BrowseRecipesView(
            self._root,
            self._show_main_view
        )
        self._current_view.pack()


    def _show_change_recipe_view(self):
        self._hide_current_view()

        self._current_view = ChangeRecipeView(
            self._root,
            self._show_main_view
            )
        self._current_view.pack()
