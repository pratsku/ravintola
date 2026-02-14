import sqlite3
from flask import Flask # type: ignore
from flask import abort, redirect, render_template, request, session # type: ignore
import config
import db
import items
import users

app = Flask(__name__)
app.secret_key = config.secret_key
app.config.setdefault("DATABASE", "database.db")

def require_login():
    if "user_id" not in session:
        abort(403)

@app.route("/")
def index():
    all_restaurants = items.get_restaurants()
    return render_template("index.html", items=all_restaurants)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    restaurants = users.get_restaurants(user_id) 
    return render_template("show_user.html", user=user, restaurants=restaurants)

@app.route("/find_item")
def find_item():
    query = request.args.get("query")
    location = request.args.get("location")
    cuisine = request.args.get("cuisine")
    if query or location or cuisine:
        results = items.find_restaurants(query=query, location=location, cuisine=cuisine)
    else:
        query = ""
        location = ""
        cuisine = ""
        results = []
    return render_template("find_item.html", query=query, location=location, cuisine=cuisine, results=results)

@app.route("/item/<int:item_id>")
def show_item(item_id):
    item = items.get_restaurant(item_id)
    if not item:
        abort(404)
    classes = items.get_classes(item_id)
    return render_template("show_item.html", item=item, classes=classes)

@app.route("/new_item")
def new_item():
    require_login()
    classes = items.get_all_classes()
    return render_template("new_item.html", classes=classes)

@app.route("/create_item", methods=["POST"])
def create_item():
    require_login()
    name = request.form.get("title")
    if len(name) > 50:
        abort(403)
    description = request.form.get("description")
    if len(description) > 1000:
        abort(403)
    location = request.form.get("location")
    category = request.form.get("category")
    user_id = session["user_id"]

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            parts = entry.split(":")
            classes.append(parts[0], parts[1])

    items.add_restaurant(name, description, location, category, user_id, classes)

    return redirect("/")

@app.route("/edit_item/<int:item_id>")
def edit_item(item_id):
    require_login()
    item = items.get_restaurant(item_id)
    if not item:
        abort(404)
    if item["owner_id"] != session["user_id"]:
        abort(403)

    all_classes = items.get_all_classes()
    classes = {}
    for my_class in all_classes:
        classes[my_class] = ""
    for entry in items.get_classes(item_id):
        classes[entry["title"]] = entry["value"]
    
    return render_template("edit_item.html", item=item, classes=classes, all_classes=all_classes)

@app.route("/update_item", methods=["POST"])
def update_item():
    require_login()
    item_id = request.form["item_id"]
    item = items.get_restaurant(item_id)
    if not item:
        abort(404)
    if item["owner_id"] != session["user_id"]:
        abort(403)

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            parts = entry.split(":")
            classes.append(parts[0], parts[1])

    name = request.form.get("title")
    description = request.form.get("description")
    location = request.form.get("location")
    category = request.form.get("category")

    items.update_restaurant(item_id, name, description, location, category, classes)

    return redirect(f"/item/{item_id}")

@app.route("/remove_item/<int:item_id>", methods=["GET", "POST"])
def remove_item(item_id):
    require_login()
    item = items.get_restaurant(item_id)
    if not item:
        abort(404)
    if item["owner_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_item.html", item=item)
    
    if request.method == "POST":
        if "remove" in request.form:
            items.remove_item(item_id)
            return redirect("/")
        else:
            return redirect(f"/item/{item_id}")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    
    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return "Tunnus luotu"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")