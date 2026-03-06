import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import api_router

app = FastAPI(title="EcoStream API")

ALLOWED_ORIGINS = os.environ.get(
    "ALLOWED_ORIGINS",
    "http://localhost:5000,http://0.0.0.0:5000"
).split(",")

# Añadir el dominio de Replit si está disponible
replit_domain = os.environ.get("REPLIT_DEV_DOMAIN")
if replit_domain:
    ALLOWED_ORIGINS.append(f"https://{replit_domain}")
    # También añadimos la versión sin https por si acaso, aunque Replit usa https
    ALLOWED_ORIGINS.append(f"http://{replit_domain}")

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
