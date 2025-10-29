import os
from datetime import datetime, timezone
from flask import Flask
from flask import render_template, redirect, request, session, url_for, abort
from werkzeug.utils import secure_filename
import users, listings, config, db



app = Flask(__name__)
app.secret_key = config.secret_key

db.init_database()

def format_time(time_string):
    return datetime.fromisoformat(time_string).strftime("%Y-%m-%d %H:%M")

@app.route("/")
def index():
    all_listings = listings.get_listings()

    listings_with_images = []
    for l in all_listings:
        listing_dict = dict(l)
        listing_dict["images"] = listings.get_listing_images(listing_dict["listing_id"])
        listings_with_images.append(listing_dict)

    return render_template("index.html", listings=listings_with_images)

@app.route("/listing/<int:listing_id>")
def show_listing(listing_id):
    listing = listings.get_listing(listing_id)
    if not listing:
        abort(404)
    comments = listings.get_comments(listing_id)
    listing_images = listings.get_listing_images(listing_id)
    return render_template("listing.html", listing=listing, comments=comments, listing_images=listing_images, users=users)

@app.route("/listing/<int:listing_id>/comment", methods=["POST"])
def add_comment(listing_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    comment_text = request.form["comment_text"].strip()
    if not comment_text:
        return redirect(url_for("show_listing", listing_id=listing_id))

    listings.add_comment(
        listing_id=listing_id,
        sender_id=session["user_id"],
        comment_text=comment_text,
        time_stamp=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    )

    return redirect(url_for("show_listing", listing_id=listing_id))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid credentials", title="Login")

    return render_template("login.html", title="Login")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Include more complex requirements
        if not username or not password:
            return render_template("register.html", error="Please fill in all fields,",
                                   title="Register")
        if users.username_exists(username):
            return render_template("register.html", error="Username already taken.",
                                   title="Register")
        if password != confirm_password:
            return render_template("register.html", error="Passwords must match.",
                                   title="Register")

        time_stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
        users.create_user(username, password, time_stamp)
        return redirect(url_for("login"))
    return render_template("register.html", title="Register")

@app.route("/logout")
def logout():
    del session["user_id"]
    return redirect(url_for("index"))


@app.route("/profile/<int:profile_id>")
def other_profile(profile_id):
    if "user_id" not in session:
        return redirect(url_for("login"))
    username, time_stamp = users.get_profile_info(profile_id)
    if username is None:
        abort(404)

    user_listings = listings.get_user_listings(profile_id)

    listings_with_images = []
    for l in user_listings:
        listing_dict = dict(l)
        listing_dict["images"] = listings.get_listing_images(listing_dict["listing_id"])
        listings_with_images.append(listing_dict)
    return render_template("profile.html", title="Account", profile_id=profile_id,
                           username=username, time_stamp=time_stamp, listings=listings_with_images)

@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("login"))

    profile_id = session["user_id"]
    username, time_stamp = users.get_profile_info(profile_id)
    user_listings = listings.get_user_listings(profile_id)

    listings_with_images = []
    for l in user_listings:
        listing_dict = dict(l)
        listing_dict["images"] = listings.get_listing_images(listing_dict["listing_id"])
        listings_with_images.append(listing_dict)
    
    return render_template("profile.html", title="Account", profile_id=profile_id,
                           username=username, time_stamp=time_stamp, listings=listings_with_images)

@app.route("/create_listing", methods=["GET", "POST"])
def create_listing():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        price = request.form.get("price")
        category = request.form.get("category")
        location = request.form.get("location")
        images = request.files.getlist("images")

        if not title or not description or not price:
            return render_template(
                "create_listing.html",
                error="Please fill in all required fields.",
                title="Create Listing")

        listing_id = listings.create_listing(
            user_id=session["user_id"],
            title=title,
            description=description,
            price=float(price),
            category=category,
            location=location,
            time_stamp=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
        )

        for img in images:
            if img.filename != "":
                filename = f"{listing_id}_{secure_filename(img.filename)}"
                filepath = os.path.join("static/uploads", filename)
                img.save(filepath)
                listings.add_listing_image(listing_id, filename)

        return redirect(url_for("profile"))

    return render_template("create_listing.html", title="Create Listing")


@app.route("/delete_listing/<int:listing_id>", methods=["POST"])
def delete_listing(listing_id):
    if "user_id" not in session:
        return redirect("/login")

    listing = listings.get_listing(listing_id)
    if not listing:
        abort(404)

    if listing["user_id"] != session["user_id"]:
        abort(403)

    listings.delete_listing(listing_id)
    return redirect(url_for("profile"))
