## Sovelluslogiikka

![arkkitehtuuri](./kuvat/arkkitehtuuri.png)

## Päätoiminnallisuudet

### Reseptin luominen

Kun käyttäjä valitsee luoda uuden reseptin, etenee sovelluksen logiikka seuraavasti:

![sekvenssi-reseptin-lisaaminen](./kuvat/sekvenssi-reseptin-lisaaminen.png)

Käyttäjältä pyydetään reseptin nimi ja verkko-osoite, jonka jälkeen RecipeService selvittää, onko saman niminen resepti jo olemassa. Mikäli ei ole, luo RecipeService uuden reseptin ja RecipeRepository tallettaa sen tietokantaan. Käyttöliittymä pyytää käyttäjää syöttämään reseptin kategoriat. RecipeService välittää ne yksi kerrallaan RecipeRepositoriolle, joka luo kategoriat tietokantaan sekä yhdistää reseptin ja kategorioiden id:t toisiinsa.
