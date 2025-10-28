from flask import Flask
from flask import render_template, redirect, request, session
import sqlite3
import users, listings, config

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Log in check
        if True:
            return redirect("/")
        else:
            return render_template("login.html", error="Invalid credentials", title="Login")
    
    return render_template("login.html", title="Login")
