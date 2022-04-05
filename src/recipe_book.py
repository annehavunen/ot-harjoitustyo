from recipe_service import RecipeService

commands = {
    "x": "x exit",
    "1": "1 add a recipe",
    "2": "2 print recipes",
    "3": "3 remove a recipe",
}

class RecipeBook:
    def __init__(self):
        self.recipe_service = RecipeService()

    def start(self):
        print("Recipe Book")
        self.print_commands()

        while True:
            command = input("Command: ")
            if command == "x":
                break
            elif command == "1":
                self.add_recipe()
            elif command == "2":
                self.print_recipes()
            elif command == "3":
                self.remove_recipe()
            else:
                self.print_commands()
        
    def add_recipe(self):
        name = input("Name of the recipe: ")
        self.recipe_service.add_recipe(name)
    
    def print_recipes(self):
        self.recipe_service.print_recipes()

    def remove_recipe(self):
        name = input("Name of the recipe: ")
        self.recipe_service.remove_recipe(name)

    def print_commands(self):
        for command in commands:
            print(commands[command])


# if __name__ == "__main__":
#     reseptikirja = RecipeBook()
#     reseptikirja.start()