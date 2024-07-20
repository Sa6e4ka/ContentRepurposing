from Scrapping import get_users_videos
from VideoMaking import process_video
from Helps import create_dirs
from Loggs import logger

from YouTube import create_secrerts, youtube, authenticate_youtube, get_publish_times
from Gemini import authenticate_gemini, generate 

import os
import datetime


client_id = os.environ.get("GOOGLE_CLIENT_ID")
client_secret = os.environ.get("GOOGLE_CLIENT_SECRETS")
project_id = os.environ.get("GOOGLE_PROJECT_ID")

redirect_uris = [
    "http://localhost"
]

username = "balls_productions_inc2"
dirs = ["jsons", "output", "videos"]


def main(): 

    # Создание необходимых директорий 
    create_dirs(dirs_list=dirs)

    # Создание json-файла с секретами
    create_secrerts(
        client_id=client_id,
        client_secret=client_secret,
        project_id=project_id,
        redirect_uris=redirect_uris
    )

    # Аутентификация во всех нужных севисах google cloud    
    youtube_auth = authenticate_youtube()
    gemini = authenticate_gemini()  

    # Получение словаря с видео автора {"video_id" : "duration"}
    ids_dict = get_users_videos(username=username, offset="max")
    video_names = process_video(data=ids_dict, username=username)

    start_time = datetime.utcnow()
    num_videos = len(video_names)
    publish_times = get_publish_times(start_time, num_videos)


    for enum, (video_name, publish_time) in enumerate(zip(video_names, publish_times)):
        title = generate(credentials=gemini)
        youtube(
            name=video_name,
            title=title,
            description=f"meme video #{enum}",
            tags=[
                "memes",
                "funny",
                "dank memes",
                "lol",
                "hilarious",
                "viral",
                "trending",
                "lmao",
                "memevideo",
                "laugh"
            ],
            publishat=publish_time, #"2024-08-18T11:19:27.0Z"
            credentials=youtube_auth   
        )
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.error("Программа остановлена")