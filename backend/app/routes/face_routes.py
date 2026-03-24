from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services.face_service import recognize_face
from app.services.attendance_service import process_attendance
from app.models.user_model import create_user
from app.models.embedding_model import save_embedding
from app.utils.security import verify_admin

router = APIRouter()

class RegisterModel(BaseModel):
    name: str
    emp_id: str
    descriptor: list

class CheckinModel(BaseModel):
    descriptor: list
    camera_id: str = "webcam"

@router.post("/register", dependencies=[Depends(verify_admin)])
def register(data: RegisterModel):
    uid = create_user(data.name, data.emp_id)
    save_embedding(uid, data.descriptor)
    return {"status": "registered"}

@router.post("/checkin", dependencies=[Depends(verify_admin)])
def checkin(data: CheckinModel):
    user = recognize_face(data.descriptor)

    if user["score"] < 0.55:
        return {"status": "unknown"}

    return process_attendance(user, data.camera_id)