from pydantic import BaseModel
from datetime import datetime
from typing import List

class Video(BaseModel):
    id: str
    title: str
    description: str
    playlist_id: str
    updated_at: int = int(datetime.timestamp(datetime.now()))
    created_at: int = int(datetime.timestamp(datetime.now()))


class Playlist(BaseModel):
    id: str
    title: str
    description: str
    number_of_videos: int
    videos: List[str] = []
    updated_at: int = int(datetime.timestamp(datetime.now()))
    created_at: int = int(datetime.timestamp(datetime.now()))