
from datetime import datetime
import platform
from fastapi import APIRouter
router = APIRouter(
    prefix="/health",
    tags=["Health Check"]
)

@router.get("")
def health_check():
    return {
        "status": "OK",
        "message": "API is running",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }

@router.get("/info")
def info():
    return {
        "application": "Python Backend API",
        "version": "1.0.0",
        "python_version": platform.python_version(),
        "framework": "FastAPI",
        "server_time": datetime.utcnow().isoformat()
    }

@router.get("/ping")
def ping():
    return {
        "message": "pong"
    }