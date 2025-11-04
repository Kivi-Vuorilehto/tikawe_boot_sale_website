import sqlite3

DATABASE = "market.db"
def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn

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
        CREATE TABLE IF NOT EXISTS ListingCategories (
            category_id INTEGER PRIMARY KEY,
            category_name TEXT NOT NULL UNIQUE
        );""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Listings (
            listing_id INTEGER PRIMARY KEY,
            user_id INTEGER REFERENCES Users(user_id) ON DELETE CASCADE,
            title TEXT,
            description TEXT,
            price REAL,
            category INTEGER REFERENCES ListingCategories (category_id),
            location TEXT,
            time_stamp TEXT
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

    cursor.execute("""
        INSERT OR IGNORE INTO ListingCategories (category_name) VALUES
        ('Electronics'),
        ('Clothing'),
        ('Home & Garden'),
        ('Food'),
        ('Toys & Games'),
        ('Books'),
        ('Furniture'),
        ('Tools'),
        ('Sports Equipment'),
        ('Collectibles'),
        ('Other'); """)

    conn.commit()
    conn.close()

def create_indexes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""CREATE INDEX IF NOT EXISTS idx_listings_time
                   ON Listings(time_stamp);""")
    cursor.execute("""CREATE INDEX IF NOT EXISTS idx_listings_user_time
                   ON Listings (user_id, time_stamp);""")

    cursor.execute("""CREATE INDEX IF NOT EXISTS idx_listings_category_time
                   ON Listings (category, time_stamp);""")

    cursor.execute("""CREATE INDEX IF NOT EXISTS idx_listings_price
                   ON Listings (price);""")

    cursor.execute("""CREATE INDEX IF NOT EXISTS idx_listings_title_desc
                   ON Listings (title, description);""")

    cursor.execute("""CREATE INDEX IF NOT EXISTS idx_listing_images_listing
                   ON ListingImages (listing_id);""")

    cursor.execute("""CREATE INDEX IF NOT EXISTS idx_comments_listing_time
                   ON Comments (listing_id, time_stamp);""")
    cursor.execute("""CREATE INDEX IF NOT EXISTS idx_comments_sender
                   ON Comments (sender_id);""")

    conn.commit()
    conn.close()


init_database()
create_indexes()
