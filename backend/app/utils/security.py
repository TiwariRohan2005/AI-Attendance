from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, HTTPException, status
from app.services.auth_service import validate_admin

security = HTTPBasic()

def verify_admin(credentials: HTTPBasicCredentials = Depends(security)):
    if not validate_admin(credentials.username, credentials.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )
    return True