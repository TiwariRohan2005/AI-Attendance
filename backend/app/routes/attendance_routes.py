from fastapi import APIRouter, Depends
from app.models.attendance_model import get_attendance
from app.utils.security import verify_admin

router = APIRouter()

@router.get("/attendance", dependencies=[Depends(verify_admin)])
def attendance():
    rows = get_attendance()
    return {"attendance": rows}