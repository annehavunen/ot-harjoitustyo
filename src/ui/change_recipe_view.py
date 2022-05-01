from tkinter import ttk, constants
from services.recipe_service import RecipeService
import tkinter

class ChangeRecipeView:
    def __init__(self, root, handle_back):
        self.root = root
        self.handle_back = handle_back
        self.frame = None
        self.name_entry = None
        self.new_name_entry = None
        self.new_url_entry = None
        self.remove = tkinter.IntVar()
        self.change_name = tkinter.IntVar()
        self.change_url = tkinter.IntVar()
        self.recipe_service = RecipeService()

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def handle_changes(self):
        name = self.name_entry.get()
        comment_label = ttk.Label(master=self.frame, text="")
        comment_label.grid(row=9, column=0, sticky=constants.EW)
        if name == "":
            comment_label = ttk.Label(master=self.frame, text="Name cannot be empty.")
            comment_label.grid(row=9, column=0, sticky=constants.W)
        else:
            recipe_id = self.recipe_service.get_recipe_id(name)
            if recipe_id:
                if self.remove.get() == 1:
                    self.recipe_service.remove_recipe(name)
                    comment_label = ttk.Label(master=self.frame, text="Recipe removed.")
                    comment_label.grid(row=9, column=0, sticky=constants.W)
                else:
                    if self.change_url.get() == 0 and self.change_name.get() == 0:
                        comment_label = ttk.Label(master=self.frame, text="No changes to be committed.")
                        comment_label.grid(row=9, column=0, sticky=constants.W)
                    if self.change_url.get() == 1:
                        new_url = self.new_url_entry.get()
                        self.recipe_service.change_url(name, new_url)
                        comment_label = ttk.Label(master=self.frame, text="Changes committed successfully.")
                        comment_label.grid(row=9, column=0, sticky=constants.W)
                    if self.change_name.get() == 1:
                        new_name = self.new_name_entry.get()
                        if new_name == "":
                            comment_label = ttk.Label(master=self.frame, text="New name cannot be empty.")
                            comment_label.grid(row=9, column=0, sticky=constants.W)
                        else:
                            self.recipe_service.change_name(name, new_name)
                            comment_label = ttk.Label(master=self.frame, text="Changes committed successfully.")
                            comment_label.grid(row=9, column=0, sticky=constants.W)

            else:
                comment_label = ttk.Label(master=self.frame, text=f"Recipe called {name} cannot be found.")
                comment_label.grid(row=9, column=0, sticky=constants.W)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        self.name_entry = ttk.Entry(master=self.root)

        back_button = ttk.Button(
            master=self.frame,
            text="Back",
            command=self.handle_back
        )

        change_label = ttk.Label(master=self.frame, text="Write the name of the recipe you want to change:")
        self.name_entry = ttk.Entry(master=self.frame)

        change_name_box = ttk.Checkbutton(master=self.frame,
                        text='Change name',
                        variable=self.change_name,
                        onvalue=1,
                        offvalue=0)
        new_name_label = ttk.Label(master=self.frame, text="New name:")
        self.new_name_entry = ttk.Entry(master=self.frame)

        change_url_box = ttk.Checkbutton(master=self.frame,
                        text='Change URL',
                        variable=self.change_url,
                        onvalue=1,
                        offvalue=0)
        new_url_label = ttk.Label(master=self.frame, text="New URL:")
        self.new_url_entry = ttk.Entry(master=self.frame)

        remove_box = ttk.Checkbutton(master=self.frame,
                        text='Remove the recipe',
                        variable=self.remove,
                        onvalue=1,
                        offvalue=0)

        save_changes = ttk.Button(
            master=self.frame,
            text="Save changes",
            command=self.handle_changes
        )


        back_button.grid(row=0, column=0)
        change_label.grid(row=1, column=0)
        self.name_entry.grid(row=2, column=0, sticky=constants.W)

        change_name_box.grid(row=3, column=0, sticky=constants.W)
        new_name_label.grid(row=4, column=0, sticky=constants.W)
        self.new_name_entry.grid(row=4, column=1)

        change_url_box.grid(row=5, column=0, sticky=constants.W)
        new_url_label.grid(row=6, column=0, sticky=constants.W)
        self.new_url_entry.grid(row=6, column=1)

        remove_box.grid(row=7, column=0, sticky=constants.W)
        save_changes.grid(row=8, column=0)        
