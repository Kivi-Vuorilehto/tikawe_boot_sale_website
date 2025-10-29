A small website created to pass a basics of web-development and databases course.

### Description
The website is designed to host adverts for boot sales or garage sales. 
A user can post a listing on the feed which contains images, title, description, category, price and location. Thus others users can look at your items, see where they are sold and go buy them if they wish. 

A user can search the feed by category, price, creator username and title.

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
$env:FLASK_APP = "app.py"
flask run
```

The server is hosted at localhost:5000 by default.
