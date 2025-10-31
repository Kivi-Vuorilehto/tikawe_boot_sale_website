import random
import string
from datetime import datetime, timezone
import sqlite3
from db import get_connection

NUM_USERS = 1000000
NUM_LISTINGS = 500000
NUM_COMMENTS = 1000000

random.seed = 10

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def populate_users(conn):
    cursor = conn.cursor()
    print("Creating users")
    for _ in range(NUM_USERS):
        username = random_string(40)
        password_hash = random_string(40)
        time_stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
        cursor.execute("""
            INSERT OR IGNORE INTO Users (username, password_hash, time_stamp)
            VALUES (?, ?, ?)
        """, (username, password_hash, time_stamp))
    conn.commit()


def populate_listings(conn):
    cursor = conn.cursor()
    print("Creating listings")

    cursor.execute("SELECT user_id FROM Users")
    user_ids = [row["user_id"] for row in cursor.fetchall()]

    cursor.execute("SELECT category_id FROM ListingCategories")
    categories = [row["category_id"] for row in cursor.fetchall()]

    for _ in range(NUM_LISTINGS):
        user_id = random.choice(user_ids)
        title = random_string(100)
        description = random_string(2000)
        price = round(random.uniform(10, 1000), 2)
        category = random.choice(categories)
        location = random_string(20)
        time_stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")

        cursor.execute("""
            INSERT INTO Listings (user_id, title, description, price, category, location, time_stamp, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, 1)
        """, (user_id, title, description, price, category, location, time_stamp))

    conn.commit()


def populate_comments(conn):
    cursor = conn.cursor()
    print("Creating comments")

    cursor.execute("SELECT listing_id FROM Listings")
    listing_ids = [row["listing_id"] for row in cursor.fetchall()]

    cursor.execute("SELECT user_id FROM Users")
    user_ids = [row["user_id"] for row in cursor.fetchall()]

    for _ in range(NUM_COMMENTS):
        listing_id = random.choice(listing_ids)
        sender_id = random.choice(user_ids)
        comment_text = random_string(40)
        time_stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")

        cursor.execute("""
            INSERT INTO Comments (listing_id, sender_id, comment_text, time_stamp)
            VALUES (?, ?, ?, ?)
        """, (listing_id, sender_id, comment_text, time_stamp))

    conn.commit()


def main():
    conn = get_connection()
    conn.row_factory = sqlite3.Row

    populate_users(conn)
    populate_listings(conn)
    populate_comments(conn)

    conn.close()
    print("success")


if __name__ == "__main__":
    main()
