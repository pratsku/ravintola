# Ravintolahaku

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään ravintoloita, muokkaamaan ja poistamaan lisäämiään ravintoloita.
- Käyttäjä näkee sovellukseen lisätyt ravintolat (itse lisäämänsä että muiden käyttäjien lisäämät ravintolat).
- Käyttäjä pystyy etsimään ravintoloita hakusanalla, sijainnin, keittiötyypin tai muun kriteerin perusteella.
- Käyttäjä pystyy tarkastelemaan ravintolan tietoja, kuten nimeä, kuvausta ja sijaintia.
- Käyttäjä pystyy antamaan ravintoloille arvosteluja ja/tai pisteytyksiä sekä näkee muiden käyttäjien antamia arvosteluja.
- Käyttäjä pystyy valitsemaan ravintolalle yhden tai useamman luokan (esimerkiksi keittiötyyppi, hintataso tai erityisruokavaliot).

# Välipalautus 2 - 1.2.2026
Sovelluksen ominaisuudet:
- Käyttäjän rekisteröityminen ja kirjautuminen
- Ravintoloiden lisääminen nimellä, kuvauksella, sijainnilla ja yhdellä luokalla (keittiötyyppi)
- Ravintoloiden muokkaaminen ja poistaminen vain, jos olet omistaja
- Kaikkien ravintoloiden ja tietojen tarkastelu
- Ravintoloiden haku avainsanan, sijainnin ja keittiön/luokan mukaan

--- Sovelluksen asennus ---
Asenna flask-kirjasto:

$ pip install flask

Voit luoda tarvittaessa virtuaaliympäristö:

$ python3 -m venv venv

$ source venv/bin/activate

Luo tietokannan taulut SQL-skeemasta:

$ sqlite3 database.db < schema.sql

Voi käynnistää sovelluksen näin:

$ flask run

--- Sovelluksen käyttö ---
- Rekisteröidy käyttäjäksi sivulla ”Luo tunnus”
- Kirjaudu sisään ja lisää ravintola sivulla ”Lisää ravintola”
- Kun lisäät kategorian, anna yksi kategorian nimi (esim. italialainen)
- Tarkastele ravintolan tietoja ja käytä hakusivua (Etsi ravintola) suodattaaksesi hakusanojen, sijainnin tai keittiötyypin mukaan
