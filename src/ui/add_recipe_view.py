# ei ole vielä yhteydessä sovelluksen varsinaisiin toimintoihin
from tkinter import ttk, constants
#from tkinter import *
from unicodedata import category
from services.recipe_service import RecipeService
import tkinter


class AddRecipeView:
    def __init__(self, root, handle_back):
        self.root = root
        self.handle_back = handle_back
        self.frame = None
        self.name_entry = None
        self.recipe_service = RecipeService()

        self.meat_poultry_cat = tkinter.IntVar()

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
            # metodi voisi palauttaa recipe_id tai False

        print(f"Value of entry is: {recipe_name}")
        self.handle_category()

    def handle_category(self):
        if self.meat_poultry_cat.get() == 1:
            print("chosen meat and poultry")
        else:
            print("mitä ihmettä")
        

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

        # var1 = IntVar()
        # nappi1 = Checkbutton(master=self.frame, text="male", variable=var1).grid(row=0, sticky=W)
        # var2 = IntVar()
        # nappi2 = Checkbutton(master=self.frame, text="female", variable=var2).grid(row=1, sticky=W)

        categories_label = ttk.Label(master=self.frame, text="Choose the categories of the recipe:")

        checkbox = ttk.Checkbutton(master=self.frame,
                        text='Meat and poultry',
                        variable=self.meat_poultry_cat,
                        onvalue=1,
                        offvalue=0)#,
#                        command=self.handle_category)


        create = ttk.Button(
            master=self.frame,
            text="Create a recipe",
            command=self.handle_create
        )

        back.grid(row=0, column=0)
        name_label.grid(row=1, column=0)
        self.name_entry.grid(row=2, column=0)
        categories_label.grid(row=3, column=0)
        checkbox.grid(row=4, column=0)
        create.grid(row=5, column=0)        

