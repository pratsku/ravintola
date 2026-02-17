# Ravintolahaku
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään ravintoloita, muokkaamaan ja poistamaan lisäämiään ravintoloita.
- Käyttäjä näkee sovellukseen lisätyt ravintolat (itse lisäämänsä että muiden käyttäjien lisäämät ravintolat).
- Käyttäjä pystyy etsimään ravintoloita hakusanalla, sijainnin, keittiötyypin tai muun kriteerin perusteella.
- Käyttäjä pystyy tarkastelemaan ravintolan tietoja, kuten nimeä, kuvausta ja sijaintia.
- Käyttäjä pystyy antamaan ravintoloille arvosteluja ja/tai pisteytyksiä sekä näkee muiden käyttäjien antamia arvosteluja.
- Käyttäjä pystyy valitsemaan ravintolalle yhden tai useamman luokan (esimerkiksi keittiötyyppi, hintataso tai erityisruokavaliot).

# Välipalautus 3 - 15.2.2026
## Sovelluksen tähän menneessä ominaisuudet:

- Käyttäjän rekisteröityminen ja kirjautuminen
- Ravintoloiden lisääminen nimellä, kuvauksella, sijainnilla, hintatasolla ja yhdellä luokalla (keittiötyyppi)
- Ravintoloiden muokkaaminen ja poistaminen vain, jos olet lisännyt käyttäjä
- Voi tarkistaa muiden käyttäjien lisäämiä ravintoloita ja tietoja klikkaamalla heidän käyttäjän nimeä
- Voi kommentoida muiden käyttäjien lisäämiin ravintoloihin
- Ravintoloiden haku avainsanan, sijainnin ja keittiötyypin mukaan

## Sovelluksen asennus

Asenna flask-kirjasto:
```
$ pip install flask
```
Voit luoda tarvittaessa virtuaaliympäristö:
```
$ python3 -m venv venv

$ source venv/bin/activate
```
Luo tietokannan taulut SQL-skeemasta:
```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```
Voi käynnistää sovelluksen näin:
```
$ flask run
```

## Sovelluksen käyttö

- Rekisteröidy käyttäjäksi sivulla ”Luo tunnus”
- Kirjaudu sisään ja lisää ravintola sivulla ”Lisää ravintola”
- Voi etsiä lisäämiäsi ja muiden lisäättyjä ravintoloita hakutoimintoa käyttäen "Etsi ravintola" ja suodata hakusanojen, sijainnin tai keittiötyypin mukaan
- Tarkista muiden käyttäjien lisäämiä ravintoloita
- Kommentoi kohteisiin