from tkinter import ttk, constants
from services.recipe_service import RecipeService
import tkinter


class AddRecipeView:
    def __init__(self, root, handle_back):
        self.root = root
        self.handle_back = handle_back
        self.frame = None
        self.name_entry = None
        self.url_entry = None
        self.recipe_service = RecipeService()

        self.meat_poultry = tkinter.IntVar()
        self.seafood = tkinter.IntVar()
        self.vegetarian = tkinter.IntVar()
        self.snacks_side_dishes = tkinter.IntVar()
        self.desserts = tkinter.IntVar()
        self.baking = tkinter.IntVar()
        self.other = tkinter.IntVar()

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
    
    def handle_create(self):
        comment_label = ttk.Label(master=self.frame, text="")
        comment_label.grid(row=14, column=0, sticky=constants.EW)
        recipe_name = self.name_entry.get()
        if recipe_name == "":
            comment_label = ttk.Label(master=self.frame, text="Name must be at least one character long.")
            comment_label.grid(row=14, column=0, sticky=constants.W)
        else:
            recipe_url = self.url_entry.get()
            recipe_id = self.recipe_service.add_recipe(recipe_name, recipe_url)
            if recipe_id:
                categories = self.handle_categories()
                self.recipe_service.add_categories(recipe_id, categories)
                comment_label = ttk.Label(master=self.frame, text=f"Recipe '{recipe_name}' added! Return with Back.")
                comment_label.grid(row=14, column=0, sticky=constants.W)
            else:
                comment_label = ttk.Label(master=self.frame, text=f"Recipe with the name '{recipe_name}' exists already.")
                comment_label.grid(row=14, column=0, sticky=constants.W)

    def handle_categories(self):
        categories = ""
        if self.meat_poultry.get() == 1:
            categories += "1"
        if self.seafood.get() == 1:
            categories += "2"
        if self.vegetarian.get() == 1:
            categories += "3"
        if self.snacks_side_dishes.get() == 1:
            categories += "4"
        if self.desserts.get() == 1:
            categories += "5"
        if self.baking.get() == 1:
            categories += "6"
        if self.other.get() == 1:
            categories += "7"
        return categories

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        self.name_entry = ttk.Entry(master=self.root)

        back_button = ttk.Button(
            master=self.frame,
            text="Back",
            command=self.handle_back
        )

        name_label = ttk.Label(master=self.frame, text="Name of the recipe")
        self.name_entry = ttk.Entry(master=self.frame)
        url_label = ttk.Label(master=self.frame, text="URL of the recipe")
        self.url_entry = ttk.Entry(master=self.frame)

        categories_label = ttk.Label(master=self.frame, text="Choose the categories of the recipe:")
        checkbox1 = ttk.Checkbutton(master=self.frame,
                        text='Meat and poultry',
                        variable=self.meat_poultry,
                        onvalue=1,
                        offvalue=0)

        checkbox2 = ttk.Checkbutton(master=self.frame,
                        text='Seafood',
                        variable=self.seafood,
                        onvalue=1,
                        offvalue=0)

        checkbox3 = ttk.Checkbutton(master=self.frame,
                        text='Vegetarian',
                        variable=self.vegetarian,
                        onvalue=1,
                        offvalue=0)
        
        checkbox4 = ttk.Checkbutton(master=self.frame,
                        text='Snacks and side dishes',
                        variable=self.snacks_side_dishes,
                        onvalue=1,
                        offvalue=0)

        checkbox5 = ttk.Checkbutton(master=self.frame,
                        text='Desserts',
                        variable=self.desserts,
                        onvalue=1,
                        offvalue=0)

        checkbox6 = ttk.Checkbutton(master=self.frame,
                        text='Baking',
                        variable=self.baking,
                        onvalue=1,
                        offvalue=0)

        checkbox7 = ttk.Checkbutton(master=self.frame,
                        text='Other',
                        variable=self.other,
                        onvalue=1,
                        offvalue=0)

        create = ttk.Button(
            master=self.frame,
            text="Create a recipe",
            command=self.handle_create
        )

        back_button.grid(row=0, column=0)
        name_label.grid(row=1, column=0)
        self.name_entry.grid(row=2, column=0)
        url_label.grid(row=3, column=0)
        self.url_entry.grid(row=4, column=0)
        categories_label.grid(row=5, column=0)
        checkbox1.grid(row=6, column=0, sticky=constants.W)
        checkbox2.grid(row=7, column=0, sticky=constants.W)
        checkbox3.grid(row=8, column=0, sticky=constants.W)
        checkbox4.grid(row=9, column=0, sticky=constants.W)
        checkbox5.grid(row=10, column=0, sticky=constants.W)
        checkbox6.grid(row=11, column=0, sticky=constants.W)
        checkbox7.grid(row=12, column=0, sticky=constants.W)
        create.grid(row=13, column=0)        
