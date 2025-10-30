import sqlite3
from flask import g

DATABASE = "market.db"
def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn

def execute(sql, params=[]):
    conn = get_connection()
    result = conn.execute(sql, params)
    conn.commit()
    g.last_insert_id = result.lastrowid
    conn.close()

def query(sql, params=[]):
    conn = get_connection()
    result = conn.execute(sql, params).fetchall()
    conn.close()
    return result

def last_insert_id():
    return g.last_insert_id
