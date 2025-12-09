from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3, os, json, datetime
import numpy as np

DB = os.path.join(os.path.dirname(__file__), "..", "data", "attendance.db")
os.makedirs(os.path.dirname(DB), exist_ok=True)

app = FastAPI(title="Face Attendance - Windows-friendly (browser embeddings)")

# Allow all origins for demo (restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, emp_id TEXT);
    CREATE TABLE IF NOT EXISTS embeddings(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, descriptor TEXT);
    CREATE TABLE IF NOT EXISTS attendance(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, ts TEXT, camera_id TEXT, confidence REAL);
    """)
    conn.commit()
    conn.close()

@app.on_event("startup")
def startup():
    init_db()

class DescriptorModel(BaseModel):
    name: str
    emp_id: str
    descriptor: list

@app.post("/register")
async def register(payload: DescriptorModel):
    # payload has name, emp_id, descriptor (list of floats)
    conn = sqlite3.connect(DB); cur = conn.cursor()
    cur.execute("INSERT INTO users(name, emp_id) VALUES(?,?)", (payload.name, payload.emp_id))
    uid = cur.lastrowid
    cur.execute("INSERT INTO embeddings(user_id, descriptor) VALUES(?,?)", (uid, json.dumps(payload.descriptor)))
    conn.commit(); conn.close()
    return {"status":"ok","user_id": uid}

class CheckinModel(BaseModel):
    descriptor: list
    camera_id: str = "webcam"

def cosine_similarity(a, b):
    a = np.array(a); b = np.array(b)
    if np.linalg.norm(a)==0 or np.linalg.norm(b)==0:
        return 0.0
    return float(np.dot(a,b) / (np.linalg.norm(a)*np.linalg.norm(b)))

@app.post("/checkin")
async def checkin(payload: CheckinModel):
    # compare payload.descriptor to all embeddings and return best match
    conn = sqlite3.connect(DB); cur = conn.cursor()
    rows = cur.execute("SELECT e.user_id, e.descriptor, u.name FROM embeddings e JOIN users u ON e.user_id = u.id").fetchall()
    best = {"user_id": None, "name": None, "score": 0.0}
    for uid, desc_json, name in rows:
        desc = json.loads(desc_json)
        sim = cosine_similarity(payload.descriptor, desc)
        if sim > best["score"]:
            best = {"user_id": uid, "name": name, "score": sim}
    results = []
    # threshold - tune as needed; face-api.js descriptor similarity typical good threshold ~0.5-0.6
    thresh = 0.55
    if best["user_id"] and best["score"] >= thresh:
        ts = datetime.datetime.utcnow().isoformat()
        cur.execute("INSERT INTO attendance(user_id, ts, camera_id, confidence) VALUES(?,?,?,?)",
                    (best["user_id"], ts, payload.camera_id, float(best["score"])))
        conn.commit()
        results.append({"user_id": best["user_id"], "name": best["name"], "score": best["score"], "status":"matched"})
    else:
        results.append({"user_id": None, "name": None, "score": best["score"], "status":"unknown"})
    conn.close()
    return {"faces": results}

@app.get("/attendance")
async def attendance_list():
    conn = sqlite3.connect(DB); cur = conn.cursor()
    rows = cur.execute("SELECT a.id, u.name, u.emp_id, a.ts, a.confidence FROM attendance a JOIN users u ON a.user_id = u.id ORDER BY a.ts DESC").fetchall()
    conn.close()
    return {"attendance": [{"id":r[0],"name":r[1],"emp_id":r[2],"ts":r[3],"confidence":r[4]} for r in rows]}

@app.get("/users")
async def users_list():
    conn = sqlite3.connect(DB); cur = conn.cursor()
    rows = cur.execute("SELECT id, name, emp_id FROM users").fetchall()
    conn.close()
    return {"users": [{"id":r[0],"name":r[1],"emp_id":r[2]} for r in rows]}