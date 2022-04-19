class Category:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def add_id(self, id):
        self.id = id

    def __str__(self):
        return f"{self.name}"

