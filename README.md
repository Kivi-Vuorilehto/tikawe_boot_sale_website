# tikawe
A small webapp created to pass a basics of web-development and databases course.


Setup:
(For windows user PS)

python3 -m venv venv

UNIX: source venv/bin/activate
WIN: venv/Scripts/activate

pip install flask

UNIX: FLASK_APP=app.py?
UNIX: flask run

WIN: $env:FLASK_APP = "app.py"
WIN: $env:FLASK_DEBUG = "1"
WIN: flask run

server hosted at localhost:5000