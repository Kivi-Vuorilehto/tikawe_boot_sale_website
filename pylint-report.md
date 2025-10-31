# Pylint report
Pylint gives the following report from the app:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:8:0: C0410: Multiple imports on one line (users, listings, config) (multiple-imports)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:44:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:53:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:68:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:72:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:78:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:83:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:104:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:135:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:141:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:169:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:184:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:203:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:236:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:292:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:363:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:11:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:18:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:24:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module listings
listings.py:1:0: C0114: Missing module docstring (missing-module-docstring)
listings.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:7:0: R0913: Too many arguments (6/5) (too-many-arguments)
listings.py:7:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
listings.py:36:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:66:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:76:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:76:0: R0913: Too many arguments (7/5) (too-many-arguments)
listings.py:76:0: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
listings.py:86:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:86:0: R0913: Too many arguments (6/5) (too-many-arguments)
listings.py:86:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
listings.py:94:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:104:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:109:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:114:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:123:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:133:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)

------------------------------------------------------------------
Your code has been rated at 8.46/10 (previous run: 8.46/10, +0.00)
```


## Missing docstrings
Most of the pylint alerts are due to missing docstrings either on functions or on modules.

I have decided to not include them in my project.

## Multiple imports on one line
There is a single alert due to having multiple imports on one line.
```
app.py:8:0: C0410: Multiple imports on one line (users, listings, config) (multiple-imports)
```
This was a conscious decision as these are all of my first party imports in this module and I believe that the code looks more understandable this way.

## Dangerous default value [] as argument
```
db.py:11:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:18:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```
It is as seen in the course material, due to the potential for two operations on the list at once pylint flags this. However in this specific case there is no potential for danger as the function itself does not change the contents of the list. 

## Too many arguments
Pylint flags some database operation functions as having too many arguments:
```
listings.py:7:0: R0913: Too many arguments (6/5) (too-many-arguments)
listings.py:7:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
listings.py:76:0: R0913: Too many arguments (7/5) (too-many-arguments)
listings.py:76:0: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
listings.py:86:0: R0913: Too many arguments (6/5) (too-many-arguments)
listings.py:86:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
```

An example of one of the flagged functions:
```python
def create_listing(user_id, title, description, price, category, location, time_stamp=None):
    if time_stamp is None:
        time_stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    sql = """
        INSERT INTO Listings (user_id, title, description, price, category, location, time_stamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    db.execute(sql, [user_id, title, description, price, category, location, time_stamp])
    return db.last_insert_id()
```

In this case it is simply unavoidable due to the design of the tables in the database. I could create separate databases linked by a common user_id to avoid this but in my opinion that becomes much more harmful than having too many arguments due to increasing the complexity of the database design.