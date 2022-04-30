# ei ole vielä yhteydessä sovelluksen varsinaisiin toimintoihin
# lakkasi toimimasta, kun importtaa recipe_servicen
# from tkinter import Tk, ttk, constants
from ui.main_view import MainView
from ui.add_recipe_view import AddRecipeView


class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None
    
    def start(self):
        self.show_main_view()

    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = None

    def show_main_view(self):
        self.hide_current_view()
        self.current_view = MainView(self.root, self.show_add_recipe_view)
        self.current_view.pack()
    
    def show_add_recipe_view(self):
        self.hide_current_view()

        self.current_view = AddRecipeView(
            self.root,
            self.show_main_view
        )
        self.current_view.pack()


# window = Tk()
# window.title("Recipe Book")

# ui = UI(window)
# ui.start()

# window.mainloop()

# siirrä nämä:
#     def start(self):
#         heading_label = ttk.Label(master=self._root, text="Welcome to Recipe Book, where you can collect your favorite recipes from websites.")
#         # username_label = ttk.Label(master=self._root, text="Username")
#         # username_entry = ttk.Entry(master=self._root)
#         # password_label = ttk.Label(master=self._root, text="Password")
#         # password_entry = ttk.Entry(master=self._root)

#         add = ttk.Button(master=self._root, text="Add a recipe")
#         print = ttk.Button(master=self._root, text="Print recipes")
#         open = ttk.Button(master=self._root, text="Open a recipe")
#         change = ttk.Button(master=self._root, text="Change a recipe")        
#         remove = ttk.Button(master=self._root, text="Remove a recipe")

#         heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
#         # username_label.grid(padx=5, pady=5)
#         # username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
#         # password_label.grid(padx=5, pady=5)
#         # password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
#         add.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
#         print.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
#         open.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
#         change.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
#         remove.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

#         self._root.grid_columnconfigure(1, weight=1, minsize=300)

# window = Tk()
# window.title("Recipe Book")
# ui = UI(window)
# ui.start()
# window.mainloop()



#     def start(self):
#         heading_label = ttk.Label(master=self._root, text="Login")
#         username_label = ttk.Label(master=self._root, text="Username")
#         username_entry = ttk.Entry(master=self._root)
#         password_label = ttk.Label(master=self._root, text="Password")
#         password_entry = ttk.Entry(master=self._root)

#         button = ttk.Button(master=self._root, text="Button")

#         heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
#         username_label.grid(padx=5, pady=5)
#         username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
#         password_label.grid(padx=5, pady=5)
#         password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
#         button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

#         self._root.grid_columnconfigure(1, weight=1, minsize=300)

# window = Tk()
# window.title("TkInter example")
# ui = UI(window)
# ui.start()
# window.mainloop()