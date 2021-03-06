# Käyttöohje

Lataa sovelluksen lähdekoodi valitsemalla viimeisin release
ja sen jälkeen *Assets*-osion alta *Source code*.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä asenna riippuvuudet komennolla:

> poetry install

Suorita sen jälkeen alustustoimenpiteet komennolla:

> poetry run invoke build

Tämän jälkeen ohjelman voi käynnistää komennolla:

> poetry run invoke start

## Päänäkymä

Sovellus avautuu päänäkymään:

![paanakyma](./kuvat/kayttoohje-paanakyma.png)

Käyttäjä voi valita haluamansa toiminnon painiketta painamalla.

## Uuden reseptin luominen

Päänäkymästä voi siirtyä uuden reseptin luomisnäkymään painamalla painiketta "Add a recipe".

Uusi resepti luodaan syöttämällä reseptin nimi ja kategoria ja valitsemalla,
liittyykö reseptiin internet-linkki vai kirjoittaako käyttäjä reseptin itse.
Lopuksi painetaan painiketta "Create a recipe".

![reseptin-luonti](./kuvat/kayttoohje-uusi-resepti.png)

Takaisin päänäkymään pääsee painamalla painiketta "Back".

## Reseptien selaaminen

Päänäkymästä voi siirtyä reseptien selaamisnäkymään painamalla painiketta "Browse recipes".

Jokainen resepti näkyy niiden kategorioiden alla, mihin käyttäjä on reseptin sijoittanut.
Valikossa on myös vaihtoehto "show all", jolloin käyttäjä näkee kaikki lisäämänsä reseptit kerralla.
Käyttäjä voi myös avata reseptin, kirjoittamalla reseptin nimen ja painamalla "Open".
Jos reseptiin on liitetty URL-osoite, avautuu kyseinen verkkosivu.
Jos käyttäjä on kirjoittanut reseptin itse, ilmestyy resepti suurempaan, valkoiseen ikkunaan.

![reseptien-selaaminen](./kuvat/kayttoohje-reseptien-selaaminen.png)

## Reseptien muuttaminen

Päänäkymästä voi siirtyä reseptien muuttamisnäkymään painamalla painiketta "Change a recipe".
Muuttaakseen reseptiä käyttäjän täytyy kirjoittaa reseptin nimi ylimpään syötekenttään ja painaa Search.
Sen jälkeen hän valitsee pudotusvalikosta, haluaako hän muuttaa reseptin nimeä, osoitetta/ohjetta tai poistaa sen kokonaan.
Käyttäjälle ilmestyy valintaan liittyvä näkymä muutoksille.
Mikäli kaikki on kunnossa, tallentuvat muutokset painamalla painiketta "Save changes".

![reseptin-muuttaminen](./kuvat/kayttoohje-reseptin-muuttaminen.png)
