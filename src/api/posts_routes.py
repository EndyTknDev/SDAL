from fastapi import APIRouter

router = APIRouter(tags=["post"])

@router.get("")
async def get_posts():
    return {"message": "List of posts"}