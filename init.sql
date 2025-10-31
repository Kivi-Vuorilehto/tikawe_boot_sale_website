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
        ('Other');


CREATE INDEX IF NOT EXISTS idx_listings_status ON Listings(status);

CREATE INDEX IF NOT EXISTS idx_listings_user_status_time ON Listings (user_id, status, time_stamp DESC);
CREATE INDEX IF NOT EXISTS idx_listings_category_status_time ON Listings (category, status, time_stamp DESC);
CREATE INDEX IF NOT EXISTS idx_listings_price ON Listings (price);

CREATE INDEX IF NOT EXISTS idx_listing_images_listing ON ListingImages (listing_id);

CREATE INDEX IF NOT EXISTS idx_comments_listing_time ON Comments (listing_id, time_stamp ASC);
CREATE INDEX IF NOT EXISTS idx_comments_sender ON Comments (sender_id);