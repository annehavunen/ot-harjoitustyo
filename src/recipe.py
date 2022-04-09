"""A class for individual recipes"""

class Recipe:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"
