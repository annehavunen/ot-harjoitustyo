# Recipe Book

Sovelluksen avulla käyttäjän on mahdollista luoda oma reseptikirja.
Käyttäjä voi lisätä, selata ja poistaa reseptejä.
Reseptiin on mahdollista liittää URL-osoite tai ohje sekä kategorioita.
Reseptin verkkosivun tai ohjeen voi tämän jälkeen avata nimen perusteella.
Reseptejä pystyy hakemaan kategorioittain.

## Dokumentaatio

- [Käyttöohje](https://github.com/annehavunen/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

- [Vaatimusmäärittely](https://github.com/annehavunen/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Arkkitehtuurikuvaus](https://github.com/annehavunen/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

- [Testausdokumentti](https://github.com/annehavunen/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

- [Työaikakirjanpito](https://github.com/annehavunen/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

- [Changelog](https://github.com/annehavunen/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:
> poetry install

2. Suorita alustustoimenpiteet komennolla:
> poetry run invoke build

3. Käynnistä sovellus komennolla:
> poetry run invoke start

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
