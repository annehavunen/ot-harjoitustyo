from services.recipe_service import RecipeService


commands = {
    "x": "x exit",
    "1": "1 add a recipe",
    "2": "2 print recipes",
    "3": "3 remove a recipe",
    "4": "4 open a recipe"
}


class RecipeBook:
    def __init__(self):
        self.recipe_service = RecipeService()

    def start(self):
        print("Welcome to Recipe Book, where you can collect your favorite recipes from websites.")
        print("Categories will be added later.")
        print()
        print("Commands:")
        self.print_commands()
        print()

        while True:
            command = input("Command: ")
            if command == "x":
                break
            if command == "1":
                self.add_recipe()
            elif command == "2":
                self.print_recipes()
            elif command == "3":
                self.remove_recipe()
            elif command == "4":
                self.open_website()
            else:
                self.print_commands()

    def add_recipe(self):
        name = input("Name of the recipe: ")
        url = input("URL of the recipe: ")
        self.recipe_service.add_recipe(name, url)

    def print_recipes(self):
        self.recipe_service.print_recipes()

    def remove_recipe(self):
        name = input("Name of the recipe: ")
        self.recipe_service.remove_recipe(name)

    def print_commands(self):
        for command in commands.values():
            print(command)

    def open_website(self):
        title = input("Name of the recipe you want to open: ")
        self.recipe_service.open_recipe(title)
