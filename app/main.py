# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {
#         "message": "Hello FastAPI",
#         "status": "success"
#     }

# from fastapi import FastAPI
# from app.routers import health

# app = FastAPI(
#     title="Python Backend API",
#     version="1.0.0"
# )

# app.include_router(health.router)

# @app.get("/")
# def root():
#     return {
#         "message": "Welcome to Python Backend API"
#     }

from fastapi import FastAPI
from app.routers import health

app = FastAPI(
    title="Python Backend API",
    version="1.0.0"
)

app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "Welcome to Python Backend API"}

# from datetime import datetime
# import platform
# from fastapi import APIRouter

# router = APIRouter(
#     prefix="/health",
#     tags=["Health Check"]
# )

# @router.get("")
# def health_check():
#     return {
#         "status": "UP",
#         "application": "Python Backend API",
#         "version": "1.0.0",
#         "python_version": platform.python_version(),
#         "server_time": datetime.utcnow().isoformat() + "Z"
#     }