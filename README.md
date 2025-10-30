A small website created to pass a basics of web-development and databases course.

### Description
The website is designed to host adverts for boot sales, garage sales or yard sales. 

A user can register an account and log in to the site.
A user can post a listing on the feed which contains images, a title, a description, a category, a price and a location. 
A feed displays all added listings to all visitors.

A user can filter the feed by category and title.
A user can sort the feed by price and time.

Comments can also be left on listings with futher questions to the seller.

Each user has a profile in which all their listings are displayed. From here they can easily navigate to a listing and remove it if it is not revelant anymore. This is also filter-able to aid users with a large number of listings.



### Setup
(For windows users, use Powershell)

#### Unix
```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
flask run
```

#### Windows
```bash
python3 -m venv venv
venv/Scripts/activate
pip install flask
flask run
```

If you wish to re-generate the database:
```
python3 create_db.py
```

If you wish to populate the database with sample random data:
```
python3 populate_db.py
```


The server is hosted at localhost:5000 by default.