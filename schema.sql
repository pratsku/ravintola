CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE restaurants (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    location TEXT,
    category_id INTEGER REFERENCES categories(id),
    owner_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    value TEXT
);

CREATE TABLE restaurant_classes (
    id INTEGER PRIMARY KEY,
    restaurant_id INTEGER REFERENCES restaurants,
    title TEXT,
    value TEXT
);

CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL,
    user_id INTEGER REFERENCES users(id),
    restaurant_id INTEGER REFERENCES restaurants(id)
);