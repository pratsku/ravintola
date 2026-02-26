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


## Tietokannan testaaminen suurilla tietomäärillä

Voit testata sovellusta suurella tietojoukolla käyttämällä `seed.py`-skriptiä. Se lisää useita käyttäjiä, ravintoloita ja kommentteja sivutuksen ja kyselyjen suorituskyvyn testaamiseksi.

Tee uusi tietokanta:
```
$ sqlite3 database.db < schema.sql
```
Luo suuri testiaineisto. Oletusarvot luovat noin 50 käyttäjää, 200 ravintolaa per käyttäjä ja yhden kommentin per ravintola (yhteensä 10 000 ravintolaa):
```
$ python3 seed.py
```
Voit säätää `kt_lkm`- ja `ravintola_lkm_per_kt`-arvoja `seed.py`-tiedoston yläosassa testataksesi pienemmillä tai suuremmilla tietojoukoilla.

### Raportti
Loin uuuden database.db ajamalla schema.sql, init.sql ja seed.py. Käynnistin Flask-kehityspalvelimen, ja vasteaikoja mittasin curl-komennoilla indeksisivuille ja sivutetuille hakusivuille (kolme ajoa per sivu).

Testatut reitit:

Indeksisivut: /, /5, /10

Hakusivut: /find_item?query=Ravintola&page=1 ja page=3

Mitattujen vasteaikojen tulokset olivat erittäin pieniä (pääosin noin 0,0016–0,0020 sekuntia). Ensimmäinen pyyntö etusivulle ja ensimmäinen hakupyyntö olivat hieman hitaampia, mutta seuraavat ajot nopeampia, todennäköisesti välimuistin ansiosta. Tulokset osoittavat, että palvelinpuolen sivutus ja tietokannan indeksit pitävät vasteajat alle 0,01 sekunttia myös 10 000 ravintolan aineistolla.

## Koodityylin raportti

Pylint-työkalulla suoritin kaikille sovelluksen Python-tiedostoille komennolla:
```
pylint *.py
```
Lopullinen kokonaispistemäärä oli 8.59/10. Suurin osa jäljellä olevista varoituksista liittyy puuttuviin docstringeihin, pitkiin tai haarautuneisiin funktioihin ja joihinkin koodin päällekkäisyyksiin. Nämä osat jätettiin projektin lopussa ennalleen, jotta vältyttäisiin uusien virheiden tuominen muuten toimiviin ja testattuihin toimintoihin.
