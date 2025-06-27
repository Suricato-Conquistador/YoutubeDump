from dotenv import load_dotenv
from fastapi import FastAPI
from routes import video, playlist

app = FastAPI()
app.include_router(video.router, prefix="/video")
app.include_router(playlist.router, prefix="/playlist")

load_dotenv()
