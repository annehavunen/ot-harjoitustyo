from tkinter import ttk, constants
from services.recipe_service import RecipeService
import tkinter

# kirjoita reseptin nimi, jonka haluat avata
# aluksi kaikki reseptit
# vetolaatikko, josta voidaan valita tietyn kategorian reseptit
class BrowseRecipesView:
    def __init__(self, root, handle_back):
        self.root = root
        self.handle_back = handle_back
        self.frame = None
        self.name_entry = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        self.name_entry = ttk.Entry(master=self.root)

        back = ttk.Button(
            master=self.frame,
            text="Back",
            command=self.handle_back
        )

        open_label = ttk.Label(master=self.frame, text="Write the name of the recipe you want to open:")
        self.name_entry = ttk.Entry(master=self.frame)

        menu = tkinter.StringVar()
        options = [
            "show all",
            "meat and poultry",
            "seafood",
            "vegetarian",
            "snacks and side dishes",
            "desserts",
            "baking",
            "other"]
        menu.set(options[0])
        drop = tkinter.OptionMenu(self.frame, menu, *options)

        back.grid(row=0, column=0)
        open_label.grid(row=1, column=0)
        self.name_entry.grid(row=2, column=0)
        drop.grid(row=3, column=0)
