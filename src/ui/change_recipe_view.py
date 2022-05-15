from tkinter import ttk, constants
from services.recipe_service import RecipeService
import tkinter


class ChangeRecipeView:
    """Muutettavan reseptin valinnasta vastaava näkymä"""

    def __init__(self, root, handle_back):
        """Luokan konstruktori. Luo uuden näkymän reseptin muuttamiselle.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_back: Kutsuttava arvo, jota kutsutaan, kun siirrytään takaisin päänäkymään.
        """
        self._root = root
        self._handle_back = handle_back
        self._frame = None
        self._name = None

        self._name_entry = None
        self._save_changes = None
        self._directions_label = None
        self._directions_text = None
        self._new_url_entry = None
        self._new_name_entry = None
        self._drop_menu = None
        self.recipe_service = RecipeService()

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _handle_remove(self):
        """Poistaa reseptin."""
        self._remove_comment()

        self.recipe_service.remove_recipe(self._name)
        comment_label = ttk.Label(master=self._frame, text="Recipe removed.")
        comment_label.grid(row=3, column=0, sticky=constants.W, padx=5, pady=5)

    def _handle_change_directions(self):
        """Muuttaa reseptin ohjeen."""
        self._remove_comment()

        recipe_directions = self._directions_text.get("1.0", "end")
        if recipe_directions == "\n":
            comment_label = ttk.Label(master=self._frame, text=f"Directions must at least one character long.")
            comment_label.grid(row=3, sticky=constants.W, padx=5, pady=5)
        else:
            self.recipe_service.change_directions(self._name, recipe_directions)
            comment_label = ttk.Label(master=self._frame, text=f"Directions changed.")
            comment_label.grid(row=3, sticky=constants.W, padx=5, pady=5)

    def _handle_change_url(self):
        """Muuttaa reseptin osoitteen."""
        self._remove_comment()

        new_url = self._new_url_entry.get()
        if new_url == "\n":
            comment_label = ttk.Label(master=self._frame, text=f"URL must at least one character long.")
            comment_label.grid(row=3, sticky=constants.W, padx=5, pady=5)
        else:
            self.recipe_service.change_url(self._name, new_url)
            comment_label = ttk.Label(master=self._frame, text=f"URL changed.")
            comment_label.grid(row=3, sticky=constants.W, padx=5, pady=5)

    def _handle_change_name(self):
        """Muuttaa reseptin nimen."""
        self._remove_comment()

        new_name = self._new_name_entry.get()
        if new_name == "":
            comment_label = ttk.Label(master=self._frame, text=f"Name must at least one character long.")
            comment_label.grid(row=3, sticky=constants.W, padx=5, pady=5)
        else:
            new_recipe_id = self.recipe_service.get_recipe_id(new_name)
            if new_recipe_id is not None:
                comment_label = ttk.Label(master=self._frame, text=f"New name {new_name} exists already.")
                comment_label.grid(row=3, sticky=constants.W, padx=5, pady=5)
            else:
                recipe_id = self.recipe_service.get_recipe_id(self._name)
                self.recipe_service.change_name(recipe_id, new_name)
                comment_label = ttk.Label(master=self._frame, text=f"Name changed.")
                comment_label.grid(row=3, sticky=constants.W, padx=5, pady=5)
                self._name = new_name

    def _remove_comment(self):
        remove_label = ttk.Label(master=self._frame, text="")
        remove_label.grid(row=3, sticky=constants.EW)

    def _destroy_widgets(self):
        if self._new_name_entry is not None:
            self._new_name_entry.destroy()
        if self._drop_menu is not None:
            self._drop_menu.destroy()
        if self._new_url_entry is not None:
            self._new_url_entry.destroy()
        if self._directions_label is not None:
            self._directions_label.destroy()
        if self._directions_text is not None:
            self._directions_text.destroy()
        if self._save_changes is not None:
            self._save_changes.destroy()

    def _show_changes(self, selection):
        self._destroy_widgets()
        self._remove_comment()

        if selection == "Name":
            self._directions_label = ttk.Label(master=self._frame, text=f"New name:")
            self._new_name_entry = ttk.Entry(master=self._frame)

            self._directions_label.grid(row=5, sticky=constants.W, padx=5, pady=5)
            self._new_name_entry.grid(row=6, column=0, sticky=(constants.W, constants.E), padx=5)
            self._save_changes = ttk.Button(
                master=self._frame,
                text="Save changes",
                command=self._handle_change_name
            )
            self._save_changes.grid(row=7, column=0, padx=5, pady=5)

        elif selection == "Directions":
            self._directions_label = ttk.Label(master=self._frame, text=f"Directions:")
            self._directions_label.grid(row=5, sticky=constants.W, padx=5, pady=5)

            recipe_directions = self.recipe_service.get_recipe_directions(self._name)
            self._directions_text = tkinter.Text(master=self._frame)
            text = recipe_directions
            self._directions_text.insert(tkinter.END, text)
            self._directions_text.grid(row=6, column=0, padx=5, pady=5)

            self._save_changes = ttk.Button(
                master=self._frame,
                text="Save changes",
                command=self._handle_change_directions
            )
            self._save_changes.grid(row=7, column=0, padx=5, pady=5)

        elif selection == "URL":
            self._directions_label = ttk.Label(master=self._frame, text=f"New URL:")
            self._new_url_entry = ttk.Entry(master=self._frame)

            self._directions_label.grid(row=5, sticky=constants.W, padx=5, pady=5)
            self._new_url_entry.grid(row=6, column=0, sticky=(constants.W, constants.E), padx=5)
            self._save_changes = ttk.Button(
                master=self._frame,
                text="Save changes",
                command=self._handle_change_url
            )
            self._save_changes.grid(row=7, column=0, padx=5, pady=5)

        else:
            self._save_changes = ttk.Button(
                master=self._frame,
                text="Save changes",
                command=self._handle_remove
            )
            self._save_changes.grid(row=7, column=0, padx=5, pady=5)


    def _print_options(self):
        self._destroy_widgets()
        self._remove_comment()

        self._name = self._name_entry.get()
        if self._name == "":
            comment_label = ttk.Label(master=self._frame, text="Name cannot be empty.")
            comment_label.grid(row=3, sticky=constants.W, padx=5, pady=5)
        else:
            recipe_id = self.recipe_service.get_recipe_id(self._name)
            if recipe_id is not None:
                recipe_url = self.recipe_service.get_url(self._name)
                if recipe_url != "":
                    choose_change_box = tkinter.StringVar()
                    options = [
                        "Name",
                        "URL",
                        "Remove the recipe"]

                    choose_change_box.set("What do you want to change")
                    self._drop_menu = tkinter.OptionMenu(self._frame, choose_change_box, *options, command=self._show_changes)
                    self._drop_menu.grid(row=4, padx=5, pady=5)

                else:
                    choose_change_box = tkinter.StringVar()
                    options = [
                        "Name",
                        "Directions",
                        "Remove the recipe"]

                    choose_change_box.set("What do you want to change")
                    self._drop_menu = tkinter.OptionMenu(self._frame, choose_change_box, *options, command=self._show_changes)
                    self._drop_menu.grid(row=4, padx=5, pady=5)
            else:
                comment_label = ttk.Label(master=self._frame, text=f"Cannot find recipe '{self._name}'.")
                comment_label.grid(row=3, sticky=constants.W, padx=5, pady=5)           


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._name_entry = ttk.Entry(master=self._root)

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )

        change_label = ttk.Label(master=self._frame, text="Name of the recipe you want to change:")
        self._name_entry = ttk.Entry(master=self._frame)

        search_recipe_button = ttk.Button(
            master=self._frame,
            text="Search",
            command=self._print_options
        )

        back_button.grid(row=0, column=0, padx=5, pady=5)
        change_label.grid(row=1, column=0, padx=5, pady=5)
        self._name_entry.grid(row=2, column=0, sticky=(constants.E, constants.W), padx=5)
        search_recipe_button.grid(row=2, column=1, padx=5, pady=5)
