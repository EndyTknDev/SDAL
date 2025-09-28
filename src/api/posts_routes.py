from fastapi import APIRouter

router = APIRouter(tags=["post"])

@router.get("")
async def get_posts():
    return {"message": "List of posts"}

@router.post("extract/date-now")
async def extract_data():
    return {"message": "Data extracted successfully"}