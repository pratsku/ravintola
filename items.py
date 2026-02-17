
"""Restaurant and item management functions."""
import db

def get_all_classes():
    """Return all class titles and values as a dict."""
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for row in result:
        title = row["title"]
        value = row["value"]
        if title not in classes:
            classes[title] = []
        classes[title].append(value)

    return classes

def add_restaurant(name, description, location, category_name, owner_id, classes):
    """Add a new restaurant with optional classes and category."""
    # pylint: disable=too-many-arguments, too-many-positional-arguments
    if classes is None:
        classes = []
    cat_id = None
    if category_name:
        res = db.query("SELECT id FROM categories WHERE name = ?", [category_name])
        if res:
            cat_id = res[0]["id"]
        else:
            db.execute("INSERT INTO categories (name) VALUES (?)", [category_name])
            cat_id = db.last_insert_id()

    sql = (
        "INSERT INTO restaurants (name, description, location, category_id, owner_id) "
        "VALUES (?, ?, ?, ?, ?)"
    )
    db.execute(sql, [name, description, location, cat_id, owner_id])

    restaurant_id = db.last_insert_id()

    sql = "INSERT INTO restaurant_classes (restaurant_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [restaurant_id, title, value])

def get_classes(restaurant_id):
    """Return all classes for a given restaurant."""
    sql = "SELECT title, value FROM restaurant_classes WHERE restaurant_id = ?"
    return db.query(sql, [restaurant_id])

def get_restaurant(restaurant_id):
    """Return a single restaurant by id, or None if not found."""
    sql = """SELECT r.id, r.name, r.description, r.location, r.category_id, c.name AS category,
                    u.id AS owner_id, u.username
            FROM restaurants r
            LEFT JOIN categories c ON r.category_id = c.id
            JOIN users u ON r.owner_id = u.id
            WHERE r.id = ?"""
    res = db.query(sql, [restaurant_id])
    if not res:
        return None
    r = res[0]

    return {
        "id": r["id"],
        "name": r["name"],
        "description": r["description"],
        "location": r["location"],
        "category": r["category"],
        "owner_id": r["owner_id"],
        "owner_username": r["username"]
    }

def update_restaurant(restaurant_id, name, description, location, category_name, classes):
    """Update a restaurant's details and classes."""
    # pylint: disable=too-many-arguments, too-many-positional-arguments
    cat_id = None
    if category_name:
        res = db.query("SELECT id FROM categories WHERE name = ?", [category_name])
        if res:
            cat_id = res[0]["id"]
        else:
            db.execute("INSERT INTO categories (name) VALUES (?)", [category_name])
            cat_id = db.last_insert_id()

    sql = (
        "UPDATE restaurants SET name = ?, description = ?, location = ?, category_id = ? "
        "WHERE id = ?"
    )
    db.execute(sql, [name, description, location, cat_id, restaurant_id])

    sql = "DELETE FROM restaurant_classes WHERE restaurant_id = ?"
    db.execute(sql, [restaurant_id])

    sql = "INSERT INTO restaurant_classes (restaurant_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [restaurant_id, title, value])

def remove_restaurant(restaurant_id):
    """Remove a restaurant and its classes."""
    db.execute("DELETE FROM restaurant_classes WHERE restaurant_id = ?", [restaurant_id])
    db.execute("DELETE FROM restaurants WHERE id = ?", [restaurant_id])

def find_restaurants(query=None, location=None, cuisine=None):
    """Find restaurants by query, location, or cuisine."""
    clauses = []
    params = []
    if query:
        clauses.append("(r.name LIKE ? OR r.description LIKE ?)")
        like = "%" + query + "%"
        params.extend([like, like])
    if location:
        clauses.append("r.location LIKE ?")
        params.append("%" + location + "%")
    if cuisine:
        clauses.append("c.name LIKE ?")
        params.append("%" + cuisine + "%")

    where = ("WHERE " + " AND ".join(clauses)) if clauses else ""
    sql = (
        "SELECT r.id, r.name, r.location, c.name AS category "
        "FROM restaurants r "
        "LEFT JOIN categories c ON r.category_id = c.id "
        f"{where} "
        "ORDER BY r.id DESC"
    )
    return db.query(sql, params)


def add_item(title, description, user_id):
    """Add a new item (restaurant) with minimal info."""
    # pylint: disable=too-many-arguments, too-many-positional-arguments
    add_restaurant(title, description, None, None, user_id, [])

def get_items():
    """Return all items (restaurants)."""
    return get_restaurants()

def get_item(item_id):
    """Return a single item (restaurant) by id."""
    return get_restaurant(item_id)

def update_item(item_id, title, description):
    """Update an item's (restaurant's) title and description."""
    # pylint: disable=too-many-arguments, too-many-positional-arguments
    update_restaurant(item_id, title, description, None, None, [])

def remove_item(item_id):
    """Remove an item (restaurant) by id."""
    remove_restaurant(item_id)

def find_item(query):
    """Find items (restaurants) by query."""
    return find_restaurants(query=query)
