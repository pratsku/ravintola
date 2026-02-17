
"""Database utility functions for the Flask app."""
import sqlite3
from flask import g # type: ignore

def get_connection():
    """Create and return a new SQLite connection with foreign keys enabled."""
    con = sqlite3.connect("database.db")
    con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con

def execute(sql, params=None):
    """Execute a SQL statement and store the last insert id in Flask's g."""
    if params is None:
        params = []
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()

def last_insert_id():
    """Return the last insert id from the last execute call."""
    return g.last_insert_id

def query(sql, params=None):
    """Execute a SQL query and return all results."""
    if params is None:
        params = []
    con = get_connection()
    result = con.execute(sql, params).fetchall()
    con.close()
    return result
