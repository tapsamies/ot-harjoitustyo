# Ohjelmistotekniikka, harjoitustyö

## Tetris

Tetris on tietokonepeli, jossa ruudulle ilmestyvistä palikoista yritetään saada muodostettua kokonaisia vaakasuuntaisia rivejä, ilman että palikoiden korkein kohta ylittää saatavilla olevan ruudukon korkeuden. Kokonaisen vaakasuuntaisen rivin syntyessä, katoaa rivi näkyvistä ja pelaaja saa pisteitä. 



### Dokumentaatio
[Tuntikirjanpito](https://github.com/tapsamies/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Vaatimusmäärittely](https://github.com/tapsamies/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Changelog](https://github.com/tapsamies/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/tapsamies/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

### Asennus ja käyttö
 
1. Käytä tätä komentoa asennusta varten:

```bash
poetry install
```

2. Sovellusta voi nyt käyttää komennolla:

```bash
poetry run invoke start
```

3. Sovelluksen testaaminen toimii komennolla:

```bash
poetry run invoke test
```

4. Sovelluksen testien tulos toimii komennolla:

```bash
poetry run invoke coverage-report
```


