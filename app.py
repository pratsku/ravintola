
import sqlite3
import secrets
from flask import Flask # type: ignore
from flask import abort, redirect, render_template, request, session # type: ignore
import config
import items
import users
import comments

app = Flask(__name__)
app.secret_key = config.secret_key
app.config.setdefault("DATABASE", "database.db")

def check_csrf():
    if request.method == "POST":
        token_form = request.form.get("csrf_token")
        token_session = session.get("csrf_token")
        if not token_form or not token_session or token_form != token_session:
            abort(403)

def require_login():
    if "user_id" not in session:
        abort(403)

@app.route("/")
def index():
    all_restaurants = items.get_items()
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
        results = items.find_restaurants(
            query=query, location=location, cuisine=cuisine
        )
    else:
        query = ""
        location = ""
        cuisine = ""
        results = []
    return render_template(
        "find_item.html",
        query=query,
        location=location,
        cuisine=cuisine,
        results=results,
    )

@app.route("/item/<int:item_id>")
def show_item(item_id):
    item = items.get_restaurant(item_id)
    if not item:
        abort(404)
    classes = items.get_classes(item_id)
    comment_list = comments.get_comments(item_id)
    return render_template("show_item.html", item=item, classes=classes, comments=comment_list)


@app.route("/add_comment", methods=["POST"])
def add_comment():
    if "user_id" not in session:
        abort(403)
    check_csrf()
    content = request.form.get("content", "").strip()
    restaurant_id = request.form.get("restaurant_id")
    if not content or not restaurant_id:
        abort(400)
    user_id = session["user_id"]
    comments.add_comment(content, user_id, restaurant_id)
    return redirect(f"/item/{restaurant_id}")

@app.route("/new_item")
def new_item():
    require_login()
    classes = items.get_all_classes()
    return render_template("new_item.html", classes=classes)

@app.route("/create_item", methods=["POST"])
def create_item():
    require_login()
    check_csrf()
    name = request.form.get("title")
    if len(name) > 50:
        abort(403)
    description = request.form.get("description")
    if len(description) > 1000:
        abort(403)
    location = request.form.get("location")
    category = request.form.get("category")
    try:
        user_id = int(session["user_id"])
    except (KeyError, ValueError):
        abort(403)

    all_classes = items.get_all_classes()

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    try:
        items.add_restaurant(
            name, description, location, category, user_id, classes
        )
    except ValueError as e:
        return f"VIRHE: {e}"

    return redirect("/")

@app.route("/edit_item/<int:item_id>")
def edit_item(item_id):
    require_login()
    item = items.get_restaurant(item_id)
    if not item:
        abort(404)
    try:
        current_user = int(session.get("user_id"))
    except (TypeError, ValueError):
        abort(403)
    if item["owner_id"] != current_user:
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
    check_csrf()
    item_id = request.form["item_id"]
    item = items.get_restaurant(item_id)
    if not item:
        abort(404)
    try:
        current_user = int(session.get("user_id"))
    except (TypeError, ValueError):
        abort(403)
    if item["owner_id"] != current_user:
        abort(403)

    all_classes = items.get_all_classes()

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    name = request.form.get("title")
    description = request.form.get("description")
    location = request.form.get("location")
    category = request.form.get("category")

    items.update_restaurant(
        item_id, name, description, location, category, classes
    )

    return redirect(f"/item/{item_id}")

@app.route("/remove_item/<int:item_id>", methods=["GET", "POST"])
def remove_item(item_id):
    require_login()
    if request.method == "POST":
        check_csrf()
    item = items.get_restaurant(item_id)
    if not item:
        abort(404)
    try:
        current_user = int(session.get("user_id"))
    except (TypeError, ValueError):
        abort(403)
    if item["owner_id"] != current_user:
        abort(403)

    if request.method == "GET":
        return render_template("remove_item.html", item=item)

    if request.method == "POST":
        if "remove" in request.form:
            items.remove_item(item_id)
            return redirect("/")
        return redirect(f"/item/{item_id}")
    return None

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    check_csrf()
    username = request.form["username"].strip()
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if not username or not password1 or not password2:
        return "VIRHE: kaikki kentät ovat pakollisia"
    if len(username) < 3 or len(username) > 30:
        return "VIRHE: käyttäjätunnuksen tulee olla 3-30 merkkiä"
    if len(password1) < 6 or len(password1) > 100:
        return "VIRHE: salasanan tulee olla 6-100 merkkiä"
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"
    return render_template("register_success.html")

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
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        return "VIRHE: väärä tunnus tai salasana"
    return None

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")
