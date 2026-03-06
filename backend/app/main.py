import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import api_router

app = FastAPI(title="EcoStream API")

ALLOWED_ORIGINS = os.environ.get(
    "ALLOWED_ORIGINS",
    "http://localhost:5000,http://0.0.0.0:5000"
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

app.include_router(api_router)


@app.get("/")
def root():
    return {"service": "EcoStream", "docs": "/docs"}
