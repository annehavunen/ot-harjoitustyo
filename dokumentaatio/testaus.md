# Testausdokumentti

## Yksikkö- ja integraatiotestaus

Sovelluslogiikasta vastaavan RecipeService-luokan testaaminen tapahtuu TestRecipeService-luokassa.
RecipeRepository vastaa tiedon pysyväistallennuksesta, ja sitä testataan luokassa TestRecipeRepository.
Testaaminen tapahtuu ainoastaan testeihin tarkoitetuilla tiedostoilla,
joiden nimet on konfiguroitu tiedostoon *.env.test*.

Testauksen haarautumakattavuus on 96%. Käyttöliittymäkerros on jätetty testauksesta pois.

![testauskattavuus](./kuvat/testikattavuus.png)

## Järjestelmätestaus

Sovellus on haettu ja testattu [käyttöohjeessa](https://github.com/annehavunen/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) kuvatulla tavalla.

Kaikki [vaatimusmäärittelyssä](https://github.com/annehavunen/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
ja käyttöohjeessa listatut toiminnallisuudet on testattu erilaisilla syötteillä.
Syötekenttiin on annettu myös virheellisiä syötteitä, kuten tyhjiä arvoja.
