from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_db

from app.routes import auth_routes, user_routes, attendance_routes, face_routes

app = FastAPI(title="AI Biometric Attendance System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

app.include_router(auth_routes.router)
app.include_router(user_routes.router)
app.include_router(attendance_routes.router)
app.include_router(face_routes.router)