import os
from youtool import YouTube


yt = YouTube(api_keys=[os.getenv("YT_KEY")])
channel_id = yt.channel_id_from_url("https://www.youtube.com/c/EntreIrm%C3%A3oseGamesEIG")


