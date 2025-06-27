import os
from fastapi import APIRouter
from youtool import YouTube
from configurations import playlists_db
from database.schemas import PlaylistCreate, all_playlists


router = APIRouter()

@router.get("/")
async def get_playlists():
    data = playlists_db.find()
    return all_playlists(data)

@router.post("/")
async def post_playlist(playlist_data: PlaylistCreate):
    yt = YouTube(api_keys=[os.getenv("YT_KEY")])
    
    channel_id = yt.channel_id_from_url(playlist_data.url)

    playlists = list(yt.channel_playlists(channel_id))
    for playlist in playlists:
        if str(playlist['title']).strip().lower() == str(playlist_data.playlist_name).strip().lower():
            videos = list(yt.playlist_videos(playlist["id"]))
            video_ids = [video["id"] for video in videos]

            document = {
                "title": playlist["title"],
                "description": playlist["description"],
                "number_of_videos": len(video_ids),
                "videos": video_ids,
            }

            playlists_db.insert_one(document)
            print("Playlist inserida no banco de dados.")

    return {"message": "Playlists processadas com sucesso"}
