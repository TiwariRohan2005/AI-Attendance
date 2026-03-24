from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.models.user_model import create_user, get_all_users
from app.utils.security import verify_admin

router = APIRouter()

class UserModel(BaseModel):
    name: str
    emp_id: str

@router.post("/users", dependencies=[Depends(verify_admin)])
def add_user(data: UserModel):
    uid = create_user(data.name, data.emp_id)
    return {"user_id": uid}

@router.get("/users", dependencies=[Depends(verify_admin)])
def users():
    return {"users": get_all_users()}