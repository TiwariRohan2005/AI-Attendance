from app.database import get_connection

def create_user(name, emp_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users(name, emp_id) VALUES (?,?)", (name, emp_id))
    uid = cur.lastrowid
    conn.commit()
    conn.close()
    return uid

def get_all_users():
    conn = get_connection()
    cur = conn.cursor()
    rows = cur.execute("SELECT id, name, emp_id FROM users").fetchall()
    conn.close()
    return rows