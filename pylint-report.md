# Pylint raportti
Pylint antaa seuraavan raportin sovelluksesta:
```
************* Module app
app.py:36:48: C0303: Trailing whitespace (trailing-whitespace)
app.py:51:0: C0301: Line too long (110/100) (line-too-long)
app.py:138:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:194:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:249:0: C0304: Final newline missing (missing-final-newline)
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:27:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:40:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:54:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:65:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:78:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:84:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:97:11: W0718: Catching too general exception Exception (broad-exception-caught)
app.py:120:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:127:11: W0718: Catching too general exception Exception (broad-exception-caught)
app.py:142:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:151:11: W0718: Catching too general exception Exception (broad-exception-caught)
app.py:178:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:187:11: W0718: Catching too general exception Exception (broad-exception-caught)
app.py:196:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:178:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:203:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:207:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:227:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:236:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:227:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:245:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:6:0: W0611: Unused import db (unused-import)
************* Module db
db.py:18:27: C0303: Trailing whitespace (trailing-whitespace)
db.py:24:0: C0304: Final newline missing (missing-final-newline)
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module config
config.py:1:0: C0304: Final newline missing (missing-final-newline)
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module items
items.py:29:0: C0301: Line too long (111/100) (line-too-long)
items.py:83:0: C0301: Line too long (104/100) (line-too-long)
items.py:112:0: C0301: Line too long (157/100) (line-too-long)
items.py:132:0: C0304: Final newline missing (missing-final-newline)
items.py:1:0: C0114: Missing module docstring (missing-module-docstring)
items.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:17:0: R0913: Too many arguments (6/5) (too-many-arguments)
items.py:17:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
items.py:38:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:42:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:51:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:73:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:73:0: R0913: Too many arguments (6/5) (too-many-arguments)
items.py:73:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
items.py:93:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:97:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:116:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:119:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:122:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:125:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:128:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:131:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module users
users.py:20:0: W0311: Bad indentation. Found 8 spaces, expected 4 (bad-indentation)
users.py:21:0: W0311: Bad indentation. Found 8 spaces, expected 4 (bad-indentation)
users.py:22:0: W0311: Bad indentation. Found 8 spaces, expected 4 (bad-indentation)
users.py:23:0: W0311: Bad indentation. Found 12 spaces, expected 8 (bad-indentation)
users.py:25:0: W0311: Bad indentation. Found 8 spaces, expected 4 (bad-indentation)
users.py:26:0: W0311: Bad indentation. Found 8 spaces, expected 4 (bad-indentation)
users.py:27:0: W0311: Bad indentation. Found 8 spaces, expected 4 (bad-indentation)
users.py:28:0: W0311: Bad indentation. Found 13 spaces, expected 8 (bad-indentation)
users.py:29:0: W0311: Bad indentation. Found 8 spaces, expected 4 (bad-indentation)
users.py:30:0: C0304: Final newline missing (missing-final-newline)
users.py:30:0: W0311: Bad indentation. Found 13 spaces, expected 8 (bad-indentation)
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:27:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
************* Module comments
comments.py:1:0: C0114: Missing module docstring (missing-module-docstring)
comments.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
comments.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
comments.py:2:0: C0411: standard import "datetime.datetime" should be placed before first party import "db"  (wrong-import-order)
```
Käyn läpi seuraavaksi, miksi kyseisiä asioita ei ole korjattu sovelluksessa.

## Docstring-huomautukset
Suurin osa raportin huomautuksista ovat seuraavanlaisia.
```
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
```
Nämä tarkoittavat, että moduuleissa ja funktioissa ei ole docstring-kommentteja. Sovelluksen kehityksessä on tehty tietoisesti päätös, ettei käytetä docstring-kommentteja.

## Import-huomautukset
```
app.py:6:0: W0611: Unused import db (unused-import)
comments.py:2:0: C0411: standard import "datetime.datetime" should be placed before first party import "db"  (wrong-import-order)
```
Importtia db tiedostossa app.py ei ole käytetty, koska kaikki sovelluksen tietokantaoperaatiot hoidetaan items-, users- ja comments-moduulien kautta, jotka itse tuovat ja käyttävät db:tä. Tiedosto app.py kutsuu ainoastaan näiden moduulien funktioita eikä ole suoraan vuorovaikutuksessa tietokannan kanssa, joten db-importti on tarpeeton ja käyttämätön.

Toinen huomautus tarkoittaa, että tiedostossa comments.py standardikirjaston tuonnin from datetime import datetime täytyy olla ennen oman moduulin tuontia import db.

## Tarpeeton else
Raportissa on seuraavanlaisia huomautuksia else-haaroihin liittyen.
```
app.py:196:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:236:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
users.py:27:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
```
Ensimmäinen huomautus koskee seuraavaa koodia:
```
    if request.method == "POST":
        if "remove" in request.form:
            items.remove_item(item_id)
            return redirect("/")
        else:
            return redirect(f"/item/{item_id}")
```
Sama koodi olisi voinut kirjoittaa vielä tiiviimmin:
````
    if request.method == "POST":
        if "remove" in request.form:
            items.remove_item(item_id)
            return redirect("/")
        return redirect(f"/item/{item_id}")
````
Tämä huomautus tarkoittaa, että koodissa on return-lauseen jälkeen heti else-lohko, mikä on tarpeetonta. Returnin jälkeen olevaa koodia ei suoriteta, joten voi poistaa else-osan ja siirtää sen sisällön yhden sisennyksen verran vasemmalle.

## Puuttuva palautusarvo
Raportissa on seuraavanlaiset huomautukset funktion palautusarvoon liittyen:
````
app.py:178:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:227:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
````
Nämä huomautukset liittyvät tilanteeseen, jossa funktio käsittelee metodit GET ja POST mutta ei muita metodeja. Esimerkiksi ensimmäinen huomautus koskee seuraavaa funktiota:
````
@app.route("/remove_item/<int:item_id>", methods=["GET", "POST"])
def remove_item(item_id):
    """Remove a restaurant item."""
    require_login()
    if request.method == "POST":
        check_csrf()
    item = items.get_restaurant(item_id)
    if not item:
        abort(404)
    try:
        current_user = int(session.get("user_id"))
    except (TypeError, ValueError):
        abort(403)
    if item["owner_id"] != current_user:
        abort(403)

    if request.method == "GET":
        return render_template("remove_item.html", item=item)

    if request.method == "POST":
        if "remove" in request.form:
            items.remove_item(item_id)
            return redirect("/")
        return redirect(f"/item/{item_id}")
````
Tämä huomautus tarkoittaa, että funktiossa osa return-lauseista palauttaa arvon (esimerkiksi return redirect("/")) ja osa ei, ja Pylint vaatii niiden olevan yhdenmukaisia selkeyden ja virheiden välttämisen vuoksi. Vaikka teoriassa voisi olla mahdollista, että funktio ei palauttaisi arvoa, jos request.method olisi jotain muuta kuin GET tai POST, käytännössä näin ei voi käydä, koska funktion dekoraattori sallii vain nämä kaksi metodia. Siksi funktio päätyy aina return-lauseeseen, eikä todellista riskiä palautusarvon puuttumisesta ole.

## Vakion nimi
Raportissa on seuraavanlainen huomautus vakion nimen liittyen:
````
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
````
Tämä huomautus tarkoittaa, että muuttujan secret_key tulisi olla kirjoitettu kokonaan isoin kirjaimin, jotta se noudattaa Pythonin nimikäytäntöä vakioille. Pylint odottaa, että vakioarvot kirjoitetaan UPPER_CASE-tyyliin. Kuitenkin sovelluksen kehittäjän näkemyksen mukaan tässä tilanteessa näyttää paremmalta, että muuttujan nimi on pienillä kirjaimilla. Muuttujaa käytetään koodissa näin:
````
app.secret_key = config.secret_key
````

## Vaarallinen oletus
Raportissa on seuraavanlaiset huomautukset:
````
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
````
Ensimmäinen huomautus koskee seuraavaa koodia:
````
def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()
````
Huomautus koskee muokattavan oletusarvon, kuten [], käyttäminen funktion parametrina (esimerkiksi def execute(sql, params=[])) on vaarallista. Jos listaa muokataan, muutos säilyy seuraavissa funktiokutsuissa, mikä voi aiheuttaa vaikeasti havaittavia virheitä. Sen sijaan kannattaa käyttää oletusarvona None ja alustaa lista funktion sisällä tarvittaessa.

## Exception
Raportissa on myös Exception-lohkoon liittyviä huomautuksia.
````
app.py:97:11: W0718: Catching too general exception Exception (broad-exception-caught)
app.py:127:11: W0718: Catching too general exception Exception (broad-exception-caught)
app.py:151:11: W0718: Catching too general exception Exception (broad-exception-caught)
app.py:187:11: W0718: Catching too general exception Exception (broad-exception-caught)
````
Varoitus liittyy siihen, että koodissa käytetään pelkkää except Exception: -lohkoa, joka nappaa kaikki poikkeukset, myös sellaiset joita ei ehkä ole tarkoitus käsitellä (esimerkiksi ohjelmointivirheet tai järjestelmän keskeytykset). Olisi parempi ottaa kiinni tarkemmin määriteltyjä poikkeuksia, jotta mahdolliset bugit eivät peity ja virheenkäsittely pysyy selkeämpänä.

## Kirjoittajan virheet
Raportissa on lisäksi monta seuraavanlaisia huomautuksia:
````
app.py:51:0: C0301: Line too long (110/100) (line-too-long)
app.py:138:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:249:0: C0304: Final newline missing (missing-final-newline)
users.py:20:0: W0311: Bad indentation. Found 8 spaces, expected 4 (bad-indentation)
items.py:73:0: R0913: Too many arguments (6/5) (too-many-arguments)
items.py:73:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
````
Ensimmäinen huomautus koskee seuraavaan riviin:
````
return render_template("find_item.html", query=query, location=location, cuisine=cuisine, results=results)
````
Rivi on 110 merkkiä pitkä ja ylittää suositellun 100 merkin enimmäispituuden. Olisi selkeämpi kirjoittaa seuraavan tapaan:
````
return render_template(
    "find_item.html",
    query=query,
    location=location,
    cuisine=cuisine,
    results=results,
)
````
'Trailing whitespace (trailing-whitespace)' koskee rivin lopussa olevia ylimääräisiä välilyöntejä.

'Final newline missing (missing-final-newline)' koskee siihen, että tiedosto ei pääty rivinvaihtomerkkiin. Puuttuva lopullinen rivinvaihto ei estä koodin suorittamista.

Neljäs huomautus koskee seuraavaa funktiota:
````
def check_login(username, password):
        sql = "SELECT id, password_hash FROM users WHERE username = ?"
        result = db.query(sql, [username])
        if not result:
            return None

        user_id = result[0]["id"]
        password_hash = result[0]["password_hash"]
        if check_password_hash(password_hash, password):
             return user_id
        else:
             return None
````
Rivi on sisennetty 8 välilyönnillä, vaikka odotettu määrä on 4. Tämä meni jotenkin ohi kirjoittajalta.

Viimeiset kaksi huomautuksia liittyy seuraavan riviin:
````
def update_restaurant(restaurant_id, name, description, location, category_name, classes):
````
Funktio ottaa 6 argumenttia ja funktiokutsussa välitetään 6 positionaalista argumenttia, mikä ylittää suositellun rajan 5. Pylint ehdottaa, että liian suuri parametrimäärä tekee funktioista vaikeampia käyttää ja ylläpitää samalla heikentää koodin selkeyttä ja lisätä virhealttiutta. Tämä ei estä koodin suorittamista.