import sqlite3
from flask import g

DATABASE = "market.db"
def get_connection():
    con = sqlite3.connect(DATABASE)
    con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con

def init_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password_hash TEXT,
            time_stamp TEXT
        );""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Listings (
            listing_id INTEGER PRIMARY KEY,
            user_id INTEGER REFERENCES Users(user_id) ON DELETE CASCADE,
            title TEXT,
            description TEXT,
            price REAL,
            category TEXT,
            location TEXT,
            time_stamp TEXT,
            status INTEGER DEFAULT 1
        );""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ListingImages (
            image_id INTEGER PRIMARY KEY,
            listing_id INTEGER REFERENCES Listings(listing_id) ON DELETE CASCADE,
            image_url TEXT
        );""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Comments (
            comment_id INTEGER PRIMARY KEY,
            listing_id INTEGER REFERENCES Listings(listing_id) ON DELETE CASCADE,
            sender_id INTEGER REFERENCES Users(user_id) ON DELETE CASCADE,
            comment_text TEXT,
            time_stamp TEXT
        );""")
    conn.commit()
    conn.close()


def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()

def query(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params).fetchall()
    con.close()
    return result

def last_insert_id():
    return g.last_insert_id
