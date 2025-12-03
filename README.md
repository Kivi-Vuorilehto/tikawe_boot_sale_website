A small website created to pass a basics of web-development and databases course.

### Description
The website is designed to host listings for boot sales, garage sales or yard sales. 
A logged-in user can put up individual items and have a common location to their sale location.

#### Basic functionality

- Any user can view all listings on the index page and more specific information on the listing page.
- Any user can filter the index by category and text content.
- Any user can sort the index by price and time.

- The user can register an account and log in to the site.
- The user can post a listing on the index which contains images, a title, a description, a category, a price and a location. 

- Comments can also be left by logged-in users on listings with futher questions to the seller.

- Each registered user has a profile page in which all their listings are displayed. 
- From here they can easily navigate to a listing and remove or edit it if it is not revelant anymore. 
- The profile page is filterable and sortable in the same way as the index.


### Setup

#### Unix
```
python3 -m venv venv
source venv/bin/activate
pip install flask
sqlite3 market.db < schema.sql
sqlite3 market.db < init.sql
flask run
```

#### Windows Poweshell
To generate and populate the database without the python scripts you will need to download sqlite3 separately.

```
python3 -m venv venv
venv/Scripts/activate
pip install flask
type .\schema.sql | .\sqlite3.exe market.db
type .\init.sql | .\sqlite3.exe market.db
flask run
```

Alternatively if you wish to generate the database with a python script then run:
```
python3 create_db.py
```

If you wish to populate the database with sample random data then run:
```
python3 populate_db.py
```

The server is hosted at localhost:5000 by default.

### Generic non-comprehensive manual test procedure
#### Setup
- Run create_db.py
- Run populate_db.py
- Start the server
  
#### Index
- Navigate to localhost:5000
- Observe listings, categories, thumbnails
- Test categories as a filter
- Test a different sorting mode
- Test text search
- Test pagination
  
#### Register and login
- Navigate to /register
- Enter valid registration details
- Submit and verify success message
- Test login with valid credentials
- Test /logout
- Test duplicate username, empty field and non-matching password error messages
- Test invalid login credentials and empty field error messages
  
#### Create and edit listing
- Login and navigate to /create_listing
- Test listing creation with images > 20
- Verify error message
- Test listing creation with valid input which contains 1 < images < 20
- Verify appearance on index and /profile/id
- Click on the created listing to enter /listing/id
- Test image carousel
- Edit listing and modify description to contain newlines and add one image to listing, save listing
- Verify newlines in description and new image appearance
- Edit listing and add 20 images, verify error message
- Create comment with newlines on listing
- Verify comment and newlines
  
#### Profile
- Navigate to /profile and verify statistics of 1 current listing and 1 current comment

#### Listing deletion
- Navigate to made listing and delete listing
- Verify listing deletion


# Reports
## Pylint report
The pylint report exists with the name pylint-report.md.

## Large dataset report
### Test procedure
Use seed.py to populate a database with data. (No images in this test because I don't want to delete 1000000 images from my drive.)

Go to localhost:5000 with firefox, open the network tab, and in there the timings subtab. Refresh.

Then we continue operating the website as a normal user and noting down the results.

### Test numbers
```
1M Users
500K Listings
1M Comments
```

It took approximately 5 minutes to populate the database. The database file size was 4.624 GB.

The only valuable category in this test was the 'waiting' category and as such all of the following values reference that.
```
GET INDEX:                                                                30ms
GET REGISTER:                                                             18ms
POST REGISTER:                                                            130ms
GET LOGIN:                                                                10ms
POST LOGIN:                                                               115ms
GET INDEX:                                                                11ms
GET LISTING(ID):                                                          21ms
GET PROFILE(ID):                                                          26ms
GET CREATE_LISTING:                                                       11ms
POST CREATE_LISTING:                                                      21ms
```
All following on index:
```
GET (DEFAULT SORT (NEWEST FIRST)):                                        13ms
GET SORT OLDEST FIRST:                                                    11ms
GET SORT BY PRICE ASC:                                                    13ms
GET SORT BY PRICE DESC:                                                   13ms

GET SEARCH BY TITLE and DESC "test" SORT BY NEWEST FIRST:                 46ms
GET SEARCH BY TITLE and DESC "test" SORT BY OLDEST FIRST:                 46ms
GET SEARCH BY TITLE and DESC "test" SORT BY PRICE ASC:                    57ms

GET SEARCH BY TITLE and DESC "test" CATEGORY BOOKS SORT BY OLDEST FIRST:  60ms
GET SEARCH BY TITLE and DESC "test" CATEGORY BOOKS SORT BY PRICE ASC:     279ms
```


We can conclude that the application would perform acceptably at low-size operation, but would struggle even at mid-size numbers. This is because 50 thumbnails would be loaded per page and there would be more than a single concurrent user. Additionally the a new database connection is opened every time data is inserted which is slow. Requests could be pooled to preserve performance at higher user numbers.
