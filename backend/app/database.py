import sqlite3
from app.config import DB_PATH
import os

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        emp_id TEXT
    );

    CREATE TABLE IF NOT EXISTS embeddings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        descriptor TEXT
    );

    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        ts TEXT,
        camera_id TEXT,
        confidence REAL
    );
    """)

    conn.commit()
    conn.close()