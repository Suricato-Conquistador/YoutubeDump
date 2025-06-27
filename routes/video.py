from fastapi import APIRouter
from database.schemas import VideoCreate
from configurations import videos_db


router = APIRouter()

@router.post("/")
async def post_video(video: VideoCreate):
    try:
        document = {
            "title": video.title,
            "description": video.description,
            "playlist_id": video.playlist_id
        }

        
        pass
    except:
        pass