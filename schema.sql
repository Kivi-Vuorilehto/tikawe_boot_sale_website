CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password_hash TEXT,
            time_stamp TEXT
        );

CREATE TABLE IF NOT EXISTS ListingCategories (
	category_id INTEGER PRIMARY KEY,
	category_name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Listings (
	listing_id INTEGER PRIMARY KEY,
	user_id INTEGER REFERENCES Users(user_id) ON DELETE CASCADE,
	title TEXT,
	description TEXT,
	price REAL,
	category INTEGER REFERENCES ListingCategories (category_id),
	location TEXT,
	time_stamp TEXT,
	status INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS ListingImages (
	image_id INTEGER PRIMARY KEY,
	listing_id INTEGER REFERENCES Listings(listing_id) ON DELETE CASCADE,
	image_url TEXT
);

CREATE TABLE IF NOT EXISTS Comments (
	comment_id INTEGER PRIMARY KEY,
	listing_id INTEGER REFERENCES Listings(listing_id) ON DELETE CASCADE,
	sender_id INTEGER REFERENCES Users(user_id) ON DELETE CASCADE,
	comment_text TEXT,
	time_stamp TEXT
);