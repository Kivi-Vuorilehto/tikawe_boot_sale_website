import os
import random
import string
import shutil
from datetime import datetime, timezone
import sqlite3
from db import get_connection

IMAGE_FOLDER = "sample_images"
UPLOAD_FOLDER = "static/uploads"

IMAGE_PREFIX = "Beagle_"
IMAGE_COUNT = 100

NUM_USERS = 10
NUM_LISTINGS = 50
NUM_COMMENTS = 10


def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def copy_image_to_listing(listing_id, image_name):
    src_path = os.path.join(IMAGE_FOLDER, image_name)
    dest_dir = os.path.join(UPLOAD_FOLDER)
    dest_path = os.path.join(dest_dir + "/" + str(listing_id) + "_" + image_name)

    if os.path.exists(src_path):
        shutil.copyfile(src_path, dest_path)
        return os.path.relpath(dest_path, UPLOAD_FOLDER)
    return None


def populate_users(conn):
    cursor = conn.cursor()
    print("Creating users")
    for _ in range(NUM_USERS):
        username = random_string(10)
        password_hash = random_string(30)
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
        title = random_string(30)
        description = random_string(200)
        price = round(random.uniform(10, 1000), 2)
        category = random.choice(categories)
        location = random_string(20)
        time_stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")

        cursor.execute("""
            INSERT INTO Listings (user_id, title, description, price, category, location, time_stamp, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, 1)
        """, (user_id, title, description, price, category, location, time_stamp))

        listing_id = cursor.lastrowid

        num_images = random.randint(1, 5)
        for _ in range(num_images):
            image_number = random.randint(1, IMAGE_COUNT)
            image_name = f"{IMAGE_PREFIX}{image_number}.jpg"

            copied_path = copy_image_to_listing(listing_id, image_name)
            if copied_path:
                cursor.execute("""
                    INSERT INTO ListingImages (listing_id, image_url)
                    VALUES (?, ?)
                """, (listing_id, copied_path))

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
