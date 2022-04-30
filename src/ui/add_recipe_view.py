# ei ole vielä yhteydessä sovelluksen varsinaisiin toimintoihin
from tkinter import ttk, constants
from services.recipe_service import RecipeService


class AddRecipeView:
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
    
    def handle_create(self):
        recipe_name = self.name_entry.get()
        recipe_id = self.recipe_service.add_recipe(recipe_name, "osoite")
        if recipe_id:
            print(recipe_id)
        else:
            print("exists already")
        # testi: lisätään resepti, asetetaan tietokantaan, ilmoittaa jos on jo

        print(f"Value of entry is: {recipe_name}")
    
    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        self.name_entry = ttk.Entry(master=self.root)

        back = ttk.Button(
            master=self.frame,
            text="Back",
            command=self.handle_back
        )

        name_label = ttk.Label(master=self.frame, text="Name of the recipe")
        self.name_entry = ttk.Entry(master=self.frame)

        create = ttk.Button(
            master=self.frame,
            text="Create a recipe",
            command=self.handle_create
        )

        back.grid(row=0, column=0)
        name_label.grid(row=1, column=0)
        self.name_entry.grid(row=2, column=0)
        create.grid(row=3, column=0)

