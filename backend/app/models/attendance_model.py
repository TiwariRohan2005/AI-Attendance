from app.database import get_connection

def mark_attendance(user_id, ts, camera_id, confidence):
    conn = get_connection()
    cur = conn.cursor()

    # prevent duplicate
    existing = cur.execute("""
        SELECT * FROM attendance 
        WHERE user_id=? AND DATE(ts)=DATE(?)
    """, (user_id, ts)).fetchone()

    if existing:
        conn.close()
        return False

    cur.execute("""
        INSERT INTO attendance(user_id, ts, camera_id, confidence)
        VALUES (?,?,?,?)
    """, (user_id, ts, camera_id, confidence))

    conn.commit()
    conn.close()
    return True

def get_attendance():
    conn = get_connection()
    cur = conn.cursor()
    rows = cur.execute("""
        SELECT u.name, u.emp_id, a.ts
        FROM attendance a 
        JOIN users u ON a.user_id = u.id
        ORDER BY a.ts DESC
    """).fetchall()
    conn.close()
    return rows