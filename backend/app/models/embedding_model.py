import json
from app.database import get_connection

def save_embedding(user_id, descriptor):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO embeddings(user_id, descriptor) VALUES (?,?)",
        (user_id, json.dumps(descriptor))
    )
    conn.commit()
    conn.close()

def get_all_embeddings():
    conn = get_connection()
    cur = conn.cursor()
    rows = cur.execute("""
        SELECT e.user_id, e.descriptor, u.name 
        FROM embeddings e JOIN users u ON e.user_id = u.id
    """).fetchall()
    conn.close()
    return rows