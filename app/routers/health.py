
from datetime import datetime
import platform
from fastapi import APIRouter
from sqlalchemy import text
from app.core.database import engine

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

@router.get("/db")
def health_db():

    try:

        with engine.connect() as conn:

            result = conn.execute(text("SELECT NOW()"))

            return {
                "status": "Connected",
                "server_time": str(result.scalar())
            }

    except Exception as ex:

        return {
            "status": "Disconnected",
            "message": str(ex)
        }