from fastapi import APIRouter
from DB import cupcakes

router = APIRouter()

@router.get("/get_all")
async def get_all_cupcakes():
    return cupcakes
