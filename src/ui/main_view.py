# työstämisvaiheessa
from tkinter import ttk, constants


class MainView:
    def __init__(self, root, handle_add_recipe, handle_browse_recipes):
        self.root = root
        self.frame = None
        self.handle_add_recipe = handle_add_recipe
        self.handle_browse_recipes = handle_browse_recipes

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
    
    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        label = ttk.Label(master=self.frame, text="Welcome to Recipe Book! \nYou can collect your favorite recipes from websites.")

        add = ttk.Button(master=self.frame, text="Add a recipe", command=self.handle_add_recipe)
        print = ttk.Button(master=self.frame, text="Browse recipes", command=self.handle_browse_recipes)
        open = ttk.Button(master=self.frame, text="Open a recipe") # ehkei tarvita, jos ylempänä on hyperlinkit
        change = ttk.Button(master=self.frame, text="Change a recipe")
        remove = ttk.Button(master=self.frame, text="Remove a recipe")

        label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        add.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        print.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        open.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        change.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        remove.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self.root.grid_columnconfigure(1, weight=1, minsize=300)

