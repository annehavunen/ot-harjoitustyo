class Recipe:
    def __init__(self, name, url, id=None):
        self.name = name
        self.url = url
        self.id = id
    
    def add_id(self, id):
        self.id = id

    def __str__(self):
        return f"{self.name}"
