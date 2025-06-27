from pydantic import BaseModel
from typing import List


class VideoCreate(BaseModel):
    title: str
    description: str
    playlist_id: str


class PlaylistCreate(BaseModel):
    url: str
    playlist_name: str


def all_playlists(playlists):
    return [document_playlist(playlist) for playlist in playlists]


def document_playlist(playlist):
    return {
        "_id": str(playlist["_id"]),
        "title": str(playlist["title"]),
        "description": str(playlist["description"]),
        "number_of_videos": str(playlist["number_of_videos"]),
        "videos": [str(task) for task in playlist["videos"]]
    }