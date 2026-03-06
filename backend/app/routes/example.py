from fastapi import APIRouter

router = APIRouter()


@router.get("/example")
def example():
    return {"message": "EcoStream API", "version": "1.0"}
