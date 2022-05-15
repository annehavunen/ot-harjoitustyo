from tkinter import ttk, constants
from services.recipe_service import RecipeService
import tkinter


class BrowseRecipesView:
    """Reseptien selaamisesta vastaava näkymä."""

    def __init__(self, root, handle_back):
        """Luokan konstruktori. Luo uuden näkymän reseptien selaamiselle.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_back: Kutsuttava arvo, jota kutsutaan, kun siirrytään takaisin päänäkymään.
        """
        self._root = root
        self._handle_back = handle_back
        self._frame = None
        self._name_entry = None
        self.recipe_service = RecipeService()

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _handle_category_print(self, selection):
        """Tulostaa reseptit valitusta kategoriasta tai reseptin ohjeen."""
        if selection != "directions":
            recipes = self.recipe_service.list_by_category(selection)
            recipe_names = ""
            for recipe in recipes:
                recipe_names += recipe + "\n"
            recipes_text = tkinter.Text(master=self._frame)
            text = recipe_names
            recipes_text.insert(tkinter.END, text)
            recipes_text.grid(row=5, column=0, padx=5, pady=5)
        else:
            name = self._name_entry.get()
            recipe_directions = self.recipe_service.get_recipe_directions(name)
            directions_text = tkinter.Text(master=self._frame)
            text = recipe_directions
            directions_text.insert(tkinter.END, text)
            directions_text.grid(row=5, column=0, padx=5, pady=5)

    def _handle_open(self):
        """Avaa reseptin verkkosivun tai itse kirjoitetun ohjeen."""
        comment_label = ttk.Label(master=self._frame, text=f"")
        comment_label.grid(row=3, column=0, sticky=constants.EW)
        name = self._name_entry.get()
        recipe_id = self.recipe_service.get_recipe_id(name)
        if recipe_id:
            recipe_url = self.recipe_service.get_url(name)
            if recipe_url != "":
                self.recipe_service.open_recipe(name)
            else:
                self._handle_category_print("directions")
        else:
            comment_label = ttk.Label(master=self._frame, text=f"Can't find recipe called '{name}'")
            comment_label.grid(row=3, column=0)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )

        open_label = ttk.Label(master=self._frame, text="Write the name of the recipe you want to open:")
        self._name_entry = ttk.Entry(master=self._frame)

        open_button = ttk.Button(
            master=self._frame,
            text="Open",
            command=self._handle_open
        )

        optionmenu = tkinter.StringVar()
        options = [
            "show all",
            "meat and poultry",
            "seafood",
            "vegetarian",
            "snacks and side dishes",
            "desserts",
            "baking",
            "other"]

        optionmenu.set("Choose a category")
        drop = tkinter.OptionMenu(self._frame, optionmenu, *options, command=self._handle_category_print)

        back_button.grid(row=0, column=0, padx=5, pady=5)
        open_label.grid(row=1, column=0, padx=5, pady=5)
        self._name_entry.grid(row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        open_button.grid(row=2, column=1, padx=5, pady=5)
        drop.grid(row=4, column=0, padx=5, pady=5)
