## Sovelluslogiikka

![arkkitehtuuri](./kuvat/arkkitehtuuri.png)

## Päätoiminnallisuudet

### Reseptin luominen

Ensin käyttäjä valitsee luoda uuden reseptin ja kirjoittaa kenttiin reseptin nimen, verkko-osoitteen ja haluamansa kategoriat.
Sen jälkeen sovelluksen logiikka etenee seuraavasti:

![sekvenssi-reseptin-lisaaminen](./kuvat/sekvenssi-reseptin-lisaaminen.png)

Käyttöjärjestelmä välittää reseptin nimen ja osoitteen.
RecipeService selvittää, onko saman niminen resepti jo olemassa.
Mikäli ei ole, luo RecipeService uuden reseptin ja RecipeRepository tallentaa sen tietokantaan.
Tämän jälkeen käyttöjärjestelmä antaa reseptin kategoriat RecipeServicelle.
RecipeService luo kategoriat yksi kerrallaan, jonka jälkeen
RecipeRepository tallentaa ne tietokantaan
ja yhdistää reseptin sekä kategorian id:t toisiinsa.
