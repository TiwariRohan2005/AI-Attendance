import datetime
from app.models.attendance_model import mark_attendance

def process_attendance(user, camera_id):
    ts = datetime.datetime.utcnow().isoformat()
    success = mark_attendance(user["user_id"], ts, camera_id, user["score"])

    return {
        "name": user["name"],
        "status": "marked" if success else "already_marked",
        "score": user["score"]
    }