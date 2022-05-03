from tkinter import ttk, constants
from services.recipe_service import RecipeService
import tkinter


class AddRecipeView:
    """Reseptin lisäämisestä vastaava näkymä."""

    def __init__(self, root, handle_back):
        """Luokan konstruktori. Luo uuden näkymän reseptin lisäämiselle.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_back: Kutsuttava arvo, jota kutsutaan, kun siirrytään takaisin päänäkymään.
        """
        self._root = root
        self._handle_back = handle_back
        self._frame = None
        self._name_entry = None
        self._url_entry = None
        self.recipe_service = RecipeService()

        self.meat_poultry = tkinter.IntVar()
        self.seafood = tkinter.IntVar()
        self.vegetarian = tkinter.IntVar()
        self.snacks_side_dishes = tkinter.IntVar()
        self.desserts = tkinter.IntVar()
        self.baking = tkinter.IntVar()
        self.other = tkinter.IntVar()

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()
    
    def _handle_create(self):
        comment_label = ttk.Label(master=self._frame, text="")
        comment_label.grid(row=14, column=0, sticky=constants.EW)
        recipe_name = self._name_entry.get()
        if recipe_name == "":
            comment_label = ttk.Label(master=self._frame, text="Name must be at least one character long.")
            comment_label.grid(row=14, column=0, sticky=constants.W)
        else:
            recipe_url = self._url_entry.get()
            recipe_id = self.recipe_service.add_recipe(recipe_name, recipe_url)
            if recipe_id:
                categories = self._handle_categories()
                self.recipe_service.add_categories(recipe_id, categories)
                comment_label = ttk.Label(master=self._frame, text=f"Recipe '{recipe_name}' added! Return with Back.")
                comment_label.grid(row=14, column=0, sticky=constants.W)
            else:
                comment_label = ttk.Label(master=self._frame, text=f"Recipe with the name '{recipe_name}' exists already.")
                comment_label.grid(row=14, column=0, sticky=constants.W)

    def _handle_categories(self):
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

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._name_entry = ttk.Entry(master=self._root)

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )

        name_label = ttk.Label(master=self._frame, text="Name of the recipe")
        self._name_entry = ttk.Entry(master=self._frame)
        url_label = ttk.Label(master=self._frame, text="URL of the recipe")
        self._url_entry = ttk.Entry(master=self._frame)

        categories_label = ttk.Label(master=self._frame, text="Choose the categories of the recipe:")
        checkbox1 = ttk.Checkbutton(master=self._frame,
                        text='Meat and poultry',
                        variable=self.meat_poultry,
                        onvalue=1,
                        offvalue=0)

        checkbox2 = ttk.Checkbutton(master=self._frame,
                        text='Seafood',
                        variable=self.seafood,
                        onvalue=1,
                        offvalue=0)

        checkbox3 = ttk.Checkbutton(master=self._frame,
                        text='Vegetarian',
                        variable=self.vegetarian,
                        onvalue=1,
                        offvalue=0)
        
        checkbox4 = ttk.Checkbutton(master=self._frame,
                        text='Snacks and side dishes',
                        variable=self.snacks_side_dishes,
                        onvalue=1,
                        offvalue=0)

        checkbox5 = ttk.Checkbutton(master=self._frame,
                        text='Desserts',
                        variable=self.desserts,
                        onvalue=1,
                        offvalue=0)

        checkbox6 = ttk.Checkbutton(master=self._frame,
                        text='Baking',
                        variable=self.baking,
                        onvalue=1,
                        offvalue=0)

        checkbox7 = ttk.Checkbutton(master=self._frame,
                        text='Other',
                        variable=self.other,
                        onvalue=1,
                        offvalue=0)

        create = ttk.Button(
            master=self._frame,
            text="Create a recipe",
            command=self._handle_create
        )

        back_button.grid(row=0, column=0)
        name_label.grid(row=1, column=0)
        self._name_entry.grid(row=2, column=0)
        url_label.grid(row=3, column=0)
        self._url_entry.grid(row=4, column=0)
        categories_label.grid(row=5, column=0)
        checkbox1.grid(row=6, column=0, sticky=constants.W)
        checkbox2.grid(row=7, column=0, sticky=constants.W)
        checkbox3.grid(row=8, column=0, sticky=constants.W)
        checkbox4.grid(row=9, column=0, sticky=constants.W)
        checkbox5.grid(row=10, column=0, sticky=constants.W)
        checkbox6.grid(row=11, column=0, sticky=constants.W)
        checkbox7.grid(row=12, column=0, sticky=constants.W)
        create.grid(row=13, column=0)        
