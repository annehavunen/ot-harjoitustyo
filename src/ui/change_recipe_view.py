from tkinter import ttk, constants
from services.recipe_service import RecipeService
import tkinter


class ChangeRecipeView:
    """Reseptin muuttamisesta vastaava näkymä"""

    def __init__(self, root, handle_back):
        """Luokan konstruktori. Luo uuden näkymän reseptin muuttamiselle.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_back: Kutsuttava arvo, jota kutsutaan, kun siirrytään takaisin päänäkymään.
        """
        self._root = root
        self._handle_back = handle_back
        self._frame = None
        self._name_entry = None
        self._new_name_entry = None
        self._new_url_entry = None
        self.remove = tkinter.IntVar()
        self.change_name = tkinter.IntVar()
        self.change_url = tkinter.IntVar()
        self.recipe_service = RecipeService()

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _handle_changes(self):
        name = self._name_entry.get()
        comment_label = ttk.Label(master=self._frame, text="")
        comment_label.grid(row=9, column=0, sticky=constants.EW)
        if name == "":
            comment_label = ttk.Label(master=self._frame, text="Name cannot be empty.")
            comment_label.grid(row=9, column=0, sticky=constants.W)
        else:
            recipe_id = self.recipe_service.get_recipe_id(name)
            if recipe_id is not None:
                if self.remove.get() == 1:
                    self.recipe_service.remove_recipe(name)
                    comment_label = ttk.Label(master=self._frame, text="Recipe removed.")
                    comment_label.grid(row=9, column=0, sticky=constants.W)
                else:
                    if self.change_url.get() == 0 and self.change_name.get() == 0:
                        comment_label = ttk.Label(master=self._frame, text="Choose what changes you want to make.")
                        comment_label.grid(row=9, column=0, sticky=constants.W)
                    elif self.change_url.get() == 1 and self.change_name.get() == 0:
                        new_url = self._new_url_entry.get()
                        self.recipe_service.change_url(name, new_url)              
                        comment_label = ttk.Label(master=self._frame, text="URL changed.")
                        comment_label.grid(row=9, column=0, sticky=constants.W)
                    else:
                        new_name = self._new_name_entry.get()
                        recipe_id = self.recipe_service.get_recipe_id(new_name)
                        if new_name == "":
                            comment_label = ttk.Label(master=self._frame, text="New name cannot be empty. Please change the name.")
                            comment_label.grid(row=9, column=0, sticky=constants.W)
                        elif recipe_id is not None:
                            comment_label = ttk.Label(master=self._frame, text=f"Name '{new_name}' exists already. Please change the name.")
                            comment_label.grid(row=9, column=0, sticky=constants.W)                            
                        else:
                            if self.change_url.get() == 0 and self.change_name.get() == 1:
                                self.recipe_service.change_name(name, new_name)
                                comment_label = ttk.Label(master=self._frame, text="Name changed.")
                                comment_label.grid(row=9, column=0, sticky=constants.W)
                            else:
                                new_url = self._new_url_entry.get()
                                self.recipe_service.change_url(name, new_url)
                                self.recipe_service.change_name(name, new_name)
                                comment_label = ttk.Label(master=self._frame, text="Name and URL changed.")
                                comment_label.grid(row=9, column=0, sticky=constants.W)
            else:
                comment_label = ttk.Label(master=self._frame, text=f"Recipe called '{name}' cannot be found.")
                comment_label.grid(row=9, column=0, sticky=constants.W)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._name_entry = ttk.Entry(master=self._root)

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )

        change_label = ttk.Label(master=self._frame, text="Name of the recipe \nyou want to change:")
        self._name_entry = ttk.Entry(master=self._frame)

        change_name_box = ttk.Checkbutton(master=self._frame,
                        text='Change name',
                        variable=self.change_name,
                        onvalue=1,
                        offvalue=0)
        new_name_label = ttk.Label(master=self._frame, text="New name:")
        self._new_name_entry = ttk.Entry(master=self._frame)

        change_url_box = ttk.Checkbutton(master=self._frame,
                        text='Change URL',
                        variable=self.change_url,
                        onvalue=1,
                        offvalue=0)
        new_url_label = ttk.Label(master=self._frame, text="New URL:")
        self._new_url_entry = ttk.Entry(master=self._frame)

        remove_box = ttk.Checkbutton(master=self._frame,
                        text='Remove the recipe',
                        variable=self.remove,
                        onvalue=1,
                        offvalue=0)

        save_changes = ttk.Button(
            master=self._frame,
            text="Save changes",
            command=self._handle_changes
        )

        back_button.grid(row=0, column=0)
        change_label.grid(row=1, column=0)
        self._name_entry.grid(row=1, column=1, sticky=(constants.E, constants.W))

        change_name_box.grid(row=3, column=0, sticky=constants.W)
        new_name_label.grid(row=4, column=0, sticky=constants.W)
        self._new_name_entry.grid(row=4, column=1, sticky=(constants.E, constants.W))

        change_url_box.grid(row=5, column=0, sticky=constants.W)
        new_url_label.grid(row=6, column=0, sticky=constants.W)
        self._new_url_entry.grid(row=6, column=1, sticky=(constants.W, constants.E))

        remove_box.grid(row=7, column=0, sticky=constants.W)
        save_changes.grid(row=8, column=0)        

#        self._frame.grid_columnconfigure(1, weight=1, minsize=300) # ei näytä hyvältä
#        self._frame.grid_columnconfigure(0, weight=1, minsize=300) # ei
#        self._frame.grid_columnconfigure(1, weight=1)