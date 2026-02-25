"""Syötä tietokantaan useita merkintöjä suorituskyvyn testaamista varten.

Suorita komento:

    python3 seed.py

Se luo useita käyttäjiä, ravintoloita ja kommentteja, joiden avulla voidaan testata sivutusta
ja kyselyjen suorituskykyä. Säädä "kt_lkm" ja "ravintolat_per_kt" tarpeen mukaan.
"""

import random
import sqlite3
from datetime import datetime

db = "database.db"

kt_lkm = 50
ravintolat_per_kt = 200

def main():
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    # Luo uusia käyttäjiä
    for i in range(1, kt_lkm + 1):
        username = f"user{i}"
        password_hash = "testi_salasana"
        try:
            cur.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        except Exception:
            pass

    # Luo luokkia
    categories = ["Italialainen", "Suomalainen", "Sushi", "Meksikolainen", "Ranskalainen"]
    for category in categories:
        try:
            cur.execute("INSERT INTO categories (name) VALUES (?)", (category,))
        except Exception:
            pass

    conn.commit()

    cur.execute("SELECT id FROM users")
    users = [r[0] for r in cur.fetchall()]
    cur.execute("SELECT id, name FROM categories")
    cats = [r[0] for r in cur.fetchall()]

    for owner in users:
        for n in range(ravintolat_per_kt):
            name = f"Ravintola {owner}-{n}"
            description = "Esimerkkikuvaus\nuseilla riveillä show_lines-suodattimen testaamiseksi."
            location = random.choice(["Helsinki", "Espoo", "Tampere", "Oulu", "Turku"]) 
            category_id = random.choice(cats) if cats else None
            cur.execute(
                "INSERT INTO restaurants (name, description, location, category_id, owner_id) VALUES (?, ?, ?, ?, ?)",
                (name, description, location, category_id, owner),
            )
            rest_id = cur.lastrowid
            # Lisää yksi kommentti
            cur.execute(
                "INSERT INTO comments (content, created_at, user_id, restaurant_id) VALUES (?, ?, ?, ?)",
                ("Hyvä ravintola", datetime.now().isoformat(), random.choice(users), rest_id),
            )

    conn.commit()
    conn.close()
    print("Tietokannan täyttäminen valmis")


if __name__ == "__main__":
    main()
