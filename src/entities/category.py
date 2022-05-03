class Category:
    """Luokka, joka kuvaa yksittäistä kategoriaa.

    Attributes:
        name: Merkkijonoarvo, joka kuvaa kategorian nimeä.
    """

    def __init__(self, name):
        """Luokan konstruktori, joka luo uuden kategorian.

        Args:
            name: Merkkijonoarvo, joka kuvaa kategorian nimeä.
        """

        self.name = name

    def __str__(self):
        return f"{self.name}"
