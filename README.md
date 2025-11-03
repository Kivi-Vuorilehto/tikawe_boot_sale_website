A small website created to pass a basics of web-development and databases course.

### Description
The website is designed to host listings for boot sales, garage sales or yard sales. 
A user can put up individual items and have a common location to their sale location.

A user can register an account and log in to the site.
A user can post a listing on the feed which contains images, a title, a description, a category, a price and a location. 
A feed displays all added listings to all visitors.

A user can filter the feed by category and text content.
A user can sort the feed by price and time.

Comments can also be left on listings with futher questions to the seller.

Each user has a profile in which all their listings are displayed. From here they can easily navigate to a listing and remove it if it is not revelant anymore. This is also filter-able to aid users with a large number of listings.



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

It took approximately 5 minutes to populate the database. The database file size was 2,21 GB.

The only valuable category in this test was the 'waiting' category and as such all of the following values reference that.
```
GET INDEX:                                                                          1300ms
POST REGISTER:                                                                      123ms
GET LOGIN:                                                                          12ms
POST LOGIN                                                                          123ms
GET INDEX                                                                           1270ms
GET LISTING(ID)                                                                     0ms
GET PROFILE(ID):                                                                    11ms
GET SEARCH BY TITLE and DESC "test":                                                2380ms
GET SORT OLDEST FIRST:                                                              1280ms
GET SORT CATEGORY "BOOKS":                                                          14ms
GET SORT CATEGORY "BOOKS", SORT PRICE LOW TO HIGH:                                  156ms
GET SEARCH BY TITLE and DESC "test", SORT CATEGORY "BOOKS", SORT PRICE LOW TO HIGH: 259ms
```

From this we can conclude that operations which do not have indexes, like filtering using the LIKE operator are much slower than the operations utilizing indexes like using the category.

We can also conclude that the application would perform acceptably at low-size operation, but would significantly struggle even at these tested mid-size numbers. This is because 50 thumbnails would be loaded per page and there would be more than a single concurrent user.
