from fastapi import APIRouter
from database.schemas import all_videos
from configurations import videos_db


router = APIRouter()

@router.get("/")
async def get_videos():
    data = videos_db.find()
    return all_videos(data)
