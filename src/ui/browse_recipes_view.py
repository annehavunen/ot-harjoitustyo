from tkinter import ttk, constants
from services.recipe_service import RecipeService
import tkinter

class BrowseRecipesView:
    def __init__(self, root, handle_back):
        self.root = root
        self.handle_back = handle_back
        self.frame = None
        self.name_entry = None
        self.recipe_service = RecipeService()

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def handle_category(self, selection):
        recipes = self.recipe_service.list_by_category(selection)

        recipe_names = ""
        for recipe in recipes:
            recipe_names += recipe + "\n"
        T = tkinter.Text(master=self.frame)
        text = recipe_names
        T.insert(tkinter.END, text)
        T.grid(row=5, column=0)

    def handle_open(self):
        nimi = self.name_entry.get()
        recipe_id = self.recipe_service.get_recipe_id(nimi)
        if recipe_id:
            self.recipe_service.open_recipe(nimi)
        else:
            cant_find_label = ttk.Label(master=self.frame, text=f"Can't find recipe called {nimi}")
            cant_find_label.grid(row=3, column=0)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        back_button = ttk.Button(
            master=self.frame,
            text="Back",
            command=self.handle_back
        )

        open_label = ttk.Label(master=self.frame, text="Write the name of the recipe you want to open:")
        self.name_entry = ttk.Entry(master=self.frame)

        open_button = ttk.Button(
            master=self.frame,
            text="Open",
            command=self.handle_open
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
        drop = tkinter.OptionMenu(self.frame, optionmenu, *options, command=self.handle_category)

        back_button.grid(row=0, column=0)
        open_label.grid(row=1, column=0)
        self.name_entry.grid(row=2, column=0)
        open_button.grid(row=2, column=1)

        drop.grid(row=4, column=0)
