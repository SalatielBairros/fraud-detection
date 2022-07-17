from fastapi import APIRouter

router = APIRouter(prefix="")

@router.get("/")
def get_index():
    return {"message": "Welcome to Fraud Detection API"}
