
import sqlite3
from flask import g, current_app  # type: ignore


def get_connection():
    try:
        db_path = current_app.config.get("DATABASE", "database.db")
    except RuntimeError:
        db_path = "database.db"

    con = sqlite3.connect(db_path)
    con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con


def execute(sql, params=None):
    if params is None:
        params = []
    con = get_connection()
    cur = con.execute(sql, params)
    con.commit()
    try:
        g.last_insert_id = cur.lastrowid
    except RuntimeError:
        pass
    con.close()


def last_insert_id():
    return getattr(g, "last_insert_id", None)


def query(sql, params=None):
    if params is None:
        params = []
    con = get_connection()
    cur = con.execute(sql, params)
    result = cur.fetchall()
    con.close()
    return result
