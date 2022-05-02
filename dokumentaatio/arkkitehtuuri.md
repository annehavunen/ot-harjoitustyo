## Sovelluslogiikka

![arkkitehtuuri](./kuvat/arkkitehtuuri.png)

## Päätoiminnallisuudet

### Reseptin luominen

Ensin käyttäjä valitsee luoda uuden reseptin ja kirjoittaa kenttiin reseptin nimen, verkko-osoitteen ja haluamansa kategoriat.
Sen jälkeen sovelluksen logiikka etenee seuraavasti:

![sekvenssi-reseptin-lisaaminen](./kuvat/sekvenssi-reseptin-lisaaminen.png)

Käyttöjärjestelmä välittää reseptin nimen ja osoitteen.
RecipeService selvittää, onko saman niminen resepti jo olemassa.
Mikäli ei ole, luo RecipeService uuden reseptin ja RecipeRepository tallettaa sen tietokantaan.
Tämän jälkeen käyttöjärjestelmä antaa reseptin kategoriat RecipeServicelle.
RecipeService välittää ne yksi kerrallaan RecipeRepositoryyn,
joka luo kategoriat tietokantaan sekä yhdistää reseptin ja kategorioiden id:t toisiinsa.
