from tkinter import ttk, constants
from services.recipe_service import RecipeService
import tkinter
from tkinter.scrolledtext import ScrolledText


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
        self._type = None
        self.recipe_service = RecipeService()

        self.meat_poultry = tkinter.IntVar()
        self.seafood = tkinter.IntVar()
        self.vegetarian = tkinter.IntVar()
        self.snacks_side_dishes = tkinter.IntVar()
        self.desserts = tkinter.IntVar()
        self.baking = tkinter.IntVar()
        self.other = tkinter.IntVar()

        self.write_url = tkinter.IntVar()
        self.write_self = tkinter.IntVar()
        self._textfield = None

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
        if self._type == None:
            comment_label = ttk.Label(master=self._frame, text="Choose a type for the recipe.")
            comment_label.grid(row=12, sticky=constants.W, padx=5, pady=5)
        else:
            recipe_name = self._name_entry.get()
            if recipe_name == "":
                comment_label = ttk.Label(master=self._frame, text="Name must be at least one character long.")
                comment_label.grid(row=14, column=0, sticky=constants.W, padx=5, pady=5)
            else:
                if self._type == "url":
                    recipe_url = self._textfield.get("1.0", "end")
                    if recipe_url == "\n":
                        comment_label = ttk.Label(master=self._frame, text=f"URL must at least one character long.")
                        comment_label.grid(row=14, column=0, sticky=constants.W, padx=5, pady=5)
                    else:
                        recipe_id = self.recipe_service.add_recipe(recipe_name, recipe_url, "")
                        if recipe_id:
                            categories = self._handle_categories()
                            self.recipe_service.add_categories(recipe_id, categories)
                            comment_label = ttk.Label(master=self._frame, text=f"Recipe '{recipe_name}' added! Return with Back.")
                            comment_label.grid(row=14, column=0, sticky=constants.W, padx=5, pady=5)
                        else:
                            comment_label = ttk.Label(master=self._frame, text=f"Recipe with the name '{recipe_name}' exists already.")
                            comment_label.grid(row=14, column=0, sticky=constants.W, padx=5, pady=5)
                elif self._type == "directions":
                    recipe_directions = self._textfield.get("1.0", "end")
                    if recipe_directions == "\n":
                        comment_label = ttk.Label(master=self._frame, text=f"Directions must at least one character long.")
                        comment_label.grid(row=14, column=0, sticky=constants.W, padx=5, pady=5)
                    else:
                        recipe_id = self.recipe_service.add_recipe(recipe_name, "", recipe_directions)
                        if recipe_id:
                            categories = self._handle_categories()
                            self.recipe_service.add_categories(recipe_id, categories)
                            comment_label = ttk.Label(master=self._frame, text=f"Recipe '{recipe_name}' added! Return with Back.")
                            comment_label.grid(row=14, column=0, sticky=constants.W, padx=5, pady=5)
                        else:
                            comment_label = ttk.Label(master=self._frame, text=f"Recipe with the name '{recipe_name}' exists already.")
                            comment_label.grid(row=14, column=0, sticky=constants.W, padx=5, pady=5)

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

    def _handle_choice(self, selection):
        """Käsittelee valinnan, kirjoittaako käyttäjä reseptin vai URL-osoitteen"""
        comment_label = ttk.Label(master=self._frame, text="")
        comment_label.grid(row=12, sticky=constants.EW)
        self._textfield = ScrolledText(self._frame, wrap=tkinter.WORD)
        self._textfield.delete("1.0", "end")
        self._textfield.grid(row=13)

        if selection == "Write the recipe yourself":
            self._type = "directions"
            comment_label = ttk.Label(master=self._frame, text="Write the directions:") 
            comment_label.grid(row=12, sticky=constants.W, padx=5, pady=5)
            self._textfield = ScrolledText(self._frame, wrap=tkinter.WORD)
            self._textfield.grid(row=13, padx=5, pady=5)
        else:
            self._type = "url"
            comment_label = ttk.Label(master=self._frame, text="Write the URL:")
            comment_label.grid(row=12, sticky=constants.W, padx=5, pady=5)
            self._textfield = ScrolledText(self._frame, wrap=tkinter.WORD)
            self._textfield.grid(row=13, padx=5, pady=5)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._name_entry = ttk.Entry(master=self._root)

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )

        name_label = ttk.Label(master=self._frame, text="Name of the recipe:")
        self._name_entry = ttk.Entry(master=self._frame)

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

        optionmenu = tkinter.StringVar()
        options = ["Write the recipe yourself", "Recipe on the Internet"]
        optionmenu.set("Type of the recipe")
        drop = tkinter.OptionMenu(self._frame, optionmenu, *options, command=self._handle_choice)

        create = ttk.Button(
            master=self._frame,
            text="Create a recipe",
            command=self._handle_create
        )

        back_button.grid(row=0, column=0, padx=5, pady=5)
        name_label.grid(row=1, column=0, sticky=constants.W, padx=5, pady=5)
        self._name_entry.grid(row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)

        categories_label.grid(row=3, column=0, sticky=constants.W, padx=5, pady=5)
        checkbox1.grid(row=4, column=0, sticky=constants.W, padx=5)
        checkbox2.grid(row=5, column=0, sticky=constants.W, padx=5)
        checkbox3.grid(row=6, column=0, sticky=constants.W, padx=5)
        checkbox4.grid(row=7, column=0, sticky=constants.W, padx=5)
        checkbox5.grid(row=8, column=0, sticky=constants.W, padx=5)
        checkbox6.grid(row=9, column=0, sticky=constants.W, padx=5)
        checkbox7.grid(row=10, column=0, sticky=constants.W, padx=5)

        drop.grid(row=11, column=0, padx=5, pady=5)
#        url_label.grid(row=3, column=0, sticky=constants.W, padx=5, pady=5)
#        self._url_entry.grid(row=4, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)


        create.grid(row=15, column=0, padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=300)
