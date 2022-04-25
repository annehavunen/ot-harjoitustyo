# Recipe Book

Sovelluksen avulla käyttäjän on mahdollista luoda oma reseptikirja.
Käyttäjä voi lisätä, selata ja poistaa reseptejä.
Reseptiin on mahdollista liittää URL-osoite sekä kategorioita. Reseptin verkkosivun voi tämän jälkeen avata nimen perusteella.
Reseptejä pystyy hakemaan kategorioittain.

## Dokumentaatio

- [Vaatimusmaarittely](https://github.com/annehavunen/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Tuntikirjanpito](https://github.com/annehavunen/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

- [Changelog](https://github.com/annehavunen/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

- [Arkkitehtuurikuvaus](https://github.com/annehavunen/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:
> poetry run invoke start

### Testaus

Testit suoritetaan komennolla:
> poetry run invoke test

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:
> poetry run invoke coverage-report

Raportti generoituu *htmlcov*-hakemistoon.

### Pylint

Tiedoston [.pylintrc](https://github.com/annehavunen/ot-harjoitustyo/blob/master/.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:
> poetry run invoke lint
