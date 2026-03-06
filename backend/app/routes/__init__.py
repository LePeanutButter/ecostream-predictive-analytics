from fastapi import APIRouter

from .health import router as health_router
from .example import router as example_router
from .huella import router as huella_router

api_router = APIRouter(prefix="/api", tags=["api"])

api_router.include_router(health_router)
api_router.include_router(example_router)
api_router.include_router(huella_router)
