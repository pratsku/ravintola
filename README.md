# Ravintolahaku
## Sovelluksen ominaisuudet
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään ravintoloita, muokkaamaan ja poistamaan lisäämiään ravintoloita.
- Käyttäjä näkee sovellukseen lisätyt ravintolat (itse lisäämänsä että muiden käyttäjien lisäämät ravintolat).
- Käyttäjä pystyy etsimään ravintoloita hakusanalla, avainsanan, sijainnin, tai keittiötyypin perusteella.
- Käyttäjä pystyy tarkastelemaan ravintolan tietoja, kuten nimeä, kuvausta ja sijaintia.
- Käyttäjä pystyy valitsemaan ravintolalle yhden luokan (hintataso).
- Käyttäjä pystyy kommentoimaan muiden käyttäjien lisäämiin ravintoloihin.

## Sovelluksen asennus
Asenna flask-kirjasto:
```
$ pip install flask
```
Luo tarvittaessa virtuaaliympäristö:
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

- Luo ensin tunnus ja kirjaudu sisään. 
- Voit lisätä uuden ravintolan Lisää ravintola -lomakkeella. 
- Etsi olemassa olevia ravintoloita 'Etsi ravintola' -toiminnolla ja suodata sijainnin tai keittiön mukaan. 
- Klikkaa kohdetta nähdäksesi tiedot ja kommentoitavissa olevat kentät.