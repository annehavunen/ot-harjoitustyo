## Sovelluslogiikka

Sovelluksen looginen malli perustuu luokkiin Recipe ja Category
sekä tietokantatauluun Recipe_category, joka yhdistää reseptit ja kategoriat toisiinsa.

![arkkitehtuuri](./kuvat/arkkitehtuuri.png)

Luokka RecipeService tarjoaa metodit käyttöliittymän vaatimille toiminnoille.
Se välittää myös toiminnot RecipeRepositoryyn.

RecipeRepository tallentaa luokkiin Recipe, Category ja Recipe_category.
Se myös hakee niistä tietoa.

## Tietojen pysyväistallennus

Luokka RecipeRepository vastaa tietojen tallentamisesta SQLite-tietokantaan.
Käytössä on kolme taulua,
jotka alustetaan [initialize_database.py](https://github.com/annehavunen/ot-harjoitustyo/blob/master/src/initialize_database.py)-tiedostossa.
Reseptit tallennetaan tauluun Recipe sekä resepteihin liittyvät kategoriat tauluun Category.
Reseptien ja kategorioiden id:t saadaan yhteyteen Recipe_category-taulun avulla.

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
