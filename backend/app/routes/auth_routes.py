from fastapi import APIRouter, Depends
from app.utils.security import verify_admin

router = APIRouter()

@router.get("/login")
def login(admin=Depends(verify_admin)):
    return {"status": "success"}