class Recipe:
    """Luokka, joka kuvaa yksittäistä reseptiä.

    Attributes:
        name: Merkkijonoarvo, joka kuvaa reseptin nimeä.
        url: Merkkijonoarvo, joka kuvaa reseptin verkko-osoitetta.
    """

    def __init__(self, name, url, directions):
        """Luokan konstruktori, joka luo uuden reseptin.

        Args:
            name: Merkkijonoarvo, joka kuvaa reseptin nimeä.
            url: Merkkijonoarvo, joka kuvaa reseptin verkko-osoitetta.
            directions: Merkkijonoarvo, joka kuvaa reseptin ohjetta.
        """

        self.name = name
        self.url = url
        self.directions = directions

    def __str__(self):
        return f"{self.name}"
