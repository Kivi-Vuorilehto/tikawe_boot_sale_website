from datetime import datetime, timezone
import os
import db

IMAGEURL = "static/uploads"

def get_user_listings(user_id, category=None, search=None, sort=None):
    sql = "SELECT * FROM Listings WHERE user_id = ? AND status = 1"
    params = [user_id]
    if category:
        sql += " AND category = ?"
        params.append(category)
    if search:
        sql += " AND (title LIKE ? OR description LIKE ?)"
        params.extend([f"%{search}%", f"%{search}%"])

    if sort == "time_asc":
        sql += " ORDER BY time_stamp ASC"
    elif sort == "price_asc":
        sql += " ORDER BY price ASC"
    elif sort == "price_desc":
        sql += " ORDER BY price DESC"
    else:
        sql += " ORDER BY time_stamp DESC"
        
    return db.query(sql, params)


def get_listings(category=None, search=None, sort=None):
    sql = "SELECT * FROM Listings WHERE status = 1"
    params = []

    if category:
        sql += " AND category = ?"
        params.append(category)
    if search:
        sql += " AND (title LIKE ? OR description LIKE ?)"
        params.extend([f"%{search}%", f"%{search}%"])

    if sort == "time_asc":
        sql += " ORDER BY time_stamp ASC"
    elif sort == "price_asc":
        sql += " ORDER BY price ASC"
    elif sort == "price_desc":
        sql += " ORDER BY price DESC"
    else:
        sql += " ORDER BY time_stamp DESC"

    return db.query(sql, params)


def get_listing(listing_id):
    sql = "SELECT * FROM Listings WHERE listing_id = ?"
    result = db.query(sql, [listing_id])
    return result[0] if result else None


def create_listing(user_id, title, description, price, category, location, time_stamp=None):
    if time_stamp is None:
        time_stamp = datetime.now(timezone.utc)
    sql = """
        INSERT INTO Listings (user_id, title, description, price, category, location, time_stamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    db.execute(sql, [user_id, title, description, price, category, location, time_stamp])
    return db.last_insert_id()


def delete_listing(listing_id):
    images = get_listing_images(listing_id)
    for image in images:
        filepath = os.path.join(IMAGEURL, image["image_url"])
        if os.path.exists(filepath):
            os.remove(filepath)

    db.execute("DELETE FROM Listings WHERE listing_id = ?", [listing_id])


def add_listing_image(listing_id, image_url):
    sql = "INSERT INTO ListingImages (listing_id, image_url) VALUES (?, ?)"
    db.execute(sql, [listing_id, image_url])


def get_listing_images(listing_id):
    sql = "SELECT * FROM ListingImages WHERE listing_id = ?"
    return db.query(sql, [listing_id])


def add_comment(listing_id, sender_id, comment_text, time_stamp=None):
    if time_stamp is None:
        time_stamp = datetime.now(timezone.utc)
    sql = """
        INSERT INTO Comments (listing_id, sender_id, comment_text, 
        time_stamp) VALUES (?, ?, ?, ?)"""
    db.execute(sql, [listing_id, sender_id, comment_text, time_stamp])


def get_comments(listing_id):
    sql = """
        SELECT c.comment_id, c.comment_text, c.time_stamp, u.username, u.user_id
        FROM Comments c
        JOIN Users u ON c.sender_id = u.user_id
        WHERE c.listing_id = ?
        ORDER BY c.time_stamp ASC
    """
    return db.query(sql, [listing_id])

def get_categories():
    sql = "SELECT * FROM ListingCategories ORDER BY category_name ASC"
    return db.query(sql)
