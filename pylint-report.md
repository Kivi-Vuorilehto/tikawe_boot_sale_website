# Pylint report
Pylint gives the following report from the app:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:8:0: C0410: Multiple imports on one line (users, listings, config) (multiple-imports)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:39:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:46:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:55:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:71:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:75:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:81:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:86:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:107:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:138:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:144:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:176:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:191:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:210:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:247:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:247:0: R0911: Too many return statements (7/6) (too-many-return-statements)
app.py:313:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:313:0: R0914: Too many local variables (16/15) (too-many-locals)
app.py:313:0: R0911: Too many return statements (7/6) (too-many-return-statements)
app.py:394:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
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
listings.py:42:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:77:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:87:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:87:0: R0913: Too many arguments (7/5) (too-many-arguments)
listings.py:87:0: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
listings.py:97:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:97:0: R0913: Too many arguments (6/5) (too-many-arguments)
listings.py:97:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
listings.py:105:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:115:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:120:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:125:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:134:0: C0116: Missing function or method docstring (missing-function-docstring)
listings.py:144:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 8.52/10 (previous run: 8.49/10, +0.03)
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

## Too many return statements
```
app.py:247:0: R0911: Too many return statements (7/6) (too-many-return-statements)
app.py:313:0: R0911: Too many return statements (7/6) (too-many-return-statements)
```

This alert is due to me doing error handling within the function, instead of separating it into its own helper function. I decided to do it this way because the project is still small in size.

## Too many local variables
```
app.py:313:0: R0914: Too many local variables (16/15) (too-many-locals)
```

I decided to assign 16 values as local variables as it improves readability.

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
listings.py:87:0: R0913: Too many arguments (7/5) (too-many-arguments)
listings.py:87:0: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
listings.py:97:0: R0913: Too many arguments (6/5) (too-many-arguments)
listings.py:97:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
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