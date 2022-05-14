# Arkkitehtuurikuvaus

## Rakenne

Koodin pakkausrakenne on seuraava:

![arkkitehtuuri-pakkaus](./kuvat/arkkitehtuuri-pakkaus.png)

Pakkaus ui sisältää käyttöliittymästä vastaavan koodin.
Services sisältää sovelluslogiikasta ja repositories tiedon pysyväistallennuksesta vastaavan koodin.
Pakkauksessa entities on sovelluksen käyttämiä tietokohteita kuvastavat luokat.

## Sovelluslogiikka

Sovelluksen looginen malli perustuu luokkiin Recipe ja Category
sekä tietokantatauluun Recipe_category, joka yhdistää reseptit ja kategoriat toisiinsa.

![arkkitehtuuri](./kuvat/arkkitehtuuri.png)

Luokka RecipeService tarjoaa metodit käyttöliittymän vaatimille toiminnoille.
Se välittää myös toiminnot RecipeRepositoryyn.

RecipeRepository tallentaa tietokantatauluihin Recipe, Category ja Recipe_category.
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

### Reseptien selailu

Kun käyttäjä painaa Browse recipes -painiketta, etenee sovelluslogiikka seuraavasti:

![sekvenssi-reseptien-selailu](./kuvat/sekvenssi-reseptien-selailu.png)

Käyttöliittymä välittää käyttäjän valitseman kategorian RecipeServicelle.
joka välittää sen edelleen RecipeRepositorylle.
RecipeRepository palauttaa kaikkien kyseiseen kategoriaan liitettyjen reseptien nimet.
Mikäli käyttäjä olisi valinnut "show all", palauttaisi RecipeRepository RecipeServicen pyynnöstä kaikki tallennetut reseptit.
RecipeService palauttaa viimein nimet listana käyttöliittymälle, joka tulostaa reseptit.

## Ohjelman rakenteeseen jääneet heikkoudet

### Käyttöliittymä

Graafisen käyttöliittymän koodissa on muutamia pitkiä metodeja, joiden toiminnallisuutta voisi jakaa pienempiin osiin.
