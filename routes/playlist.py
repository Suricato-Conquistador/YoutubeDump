import os
from bson import ObjectId
from fastapi import APIRouter
from youtool import YouTube
from configurations import playlists_db, videos_db
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

            playlist_document = {
                "title": playlist["title"],
                "description": playlist["description"],
                "number_of_videos": len(video_ids),
            }

            result = playlists_db.insert_one(playlist_document)
            
            for video in videos:

                video_document = {
                    "title": video["title"],
                    "description": video["description"],
                    "playlist_id": result.inserted_id
                }

                result2 = videos_db.insert_one(video_document)
                playlists_db.update_one({"_id": ObjectId(result.inserted_id)}, {"$push": {"videos": ObjectId(result2.inserted_id)}})

            print("Playlist inserida no banco de dados.")

    return {"message": "Playlists processadas com sucesso"}
