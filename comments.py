
from datetime import datetime
import db

def add_comment(content, user_id, restaurant_id):
    sql = """
        INSERT INTO comments (content, created_at, user_id, restaurant_id)
        VALUES (?, ?, ?, ?)
    """
    db.execute(sql, [content, datetime.now().isoformat(), user_id, restaurant_id])

def get_comments(restaurant_id):
    sql = """
        SELECT c.id, c.content, c.created_at, c.user_id, u.username
        FROM comments c JOIN users u ON c.user_id = u.id
        WHERE c.restaurant_id = ?
        ORDER BY c.created_at ASC
    """
    return db.query(sql, [restaurant_id])
