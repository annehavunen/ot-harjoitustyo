from tkinter import ttk, constants


class MainView:
    """Ohjelman päävalikosta vastaava näkymä."""

    def __init__(self, root, handle_add_recipe, handle_browse_recipes, handle_change_recipe):
        """Luokan konstruktori. Luo uuden päävalikon näkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_add_recipe: Kutsuttava arvo, jota kutsutaan, kun resepti luodaan.
            handle_browse_recipes: Kutsuttava arvo, jota kutsutaan, kun reseptejä selataan.
            handle_change_recipe: Kutsuttava arvo, jota kutsutaan, kun reseptiä muokataan.
        """
        self._root = root
        self._frame = None
        self._handle_add_recipe = handle_add_recipe
        self._handle_browse_recipes = handle_browse_recipes
        self._handle_change_recipe = handle_change_recipe

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text=
        "Welcome to Recipe Book! \nYou can collect your favorite recipes from websites.")

        add = ttk.Button(master=self._frame, text="Add a recipe", command=self._handle_add_recipe)
        browse = ttk.Button(master=self._frame, text="Browse recipes", command=self._handle_browse_recipes)
        change = ttk.Button(master=self._frame, text="Change a recipe", command=self._handle_change_recipe)

        label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        add.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        browse.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        change.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
