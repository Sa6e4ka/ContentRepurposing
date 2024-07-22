from Scrapping import get_users_videos
from VideoMaking import process_video
from Helps import create_dirs
from Loggs import logger

from YouTube import create_secrerts, youtube, authenticate_youtube, get_publish_times
from Gemini import authenticate_gemini, generate 

import os
import datetime


def deploy_func(username: str, redirect_uris: list): 
    '''
    Функция для полного прохождения этапа получения и загрузки видео на ютуб   
    '''
    infos = []

    # Создание необходимых директорий 
    create_dirs(dirs_list=["jsons", "output", "videos"])

    try:
        # Получение переменных окружения
        client_id = os.environ.get("GOOGLE_CLIENT_ID")
        client_secret = os.environ.get("GOOGLE_CLIENT_SECRETS")
        project_id = os.environ.get("GOOGLE_PROJECT_ID")

        # Создание json-файла с секретами
        create_secrerts(
            client_id=client_id,
            client_secret=client_secret,
            project_id=project_id,
            redirect_uris=redirect_uris
        )
    except:
        message = "Ошибка в получении переменных окружения"
        logger.error(message)
        return {"message" : message}

    try:
        # Аутентификация во всех нужных севисах google cloud
        youtube_auth = authenticate_youtube()
        gemini = authenticate_gemini()
        logger.info("Авторизация в сервисах Google прошла успешно")
    except:
        message = "Ошибка при авторизации в Google сервисах"
        logger.error(message)
        return {"message" : message}

    try:
        # Получение словаря с видео автора {"video_id" : "duration"}
        ids_dict = get_users_videos(username=username, offset="max")
        #Процессинг видео: скачивание, склейка, удаление 
        video_names = process_video(data=ids_dict, username=username)
        logger.info("Информация о видео успешно получена, видео успешно скачаны и склеены!")
    except:
        message = "Ошибка при процессинге видео!"
        logger.error(message)
        return {"message" : message}

    num_videos = len(video_names)
    start = datetime.datetime.now().timestamp()
    publish_times = get_publish_times(amount=num_videos, interval=12)

    for enum, (video_name, publish_time) in enumerate(zip(video_names, publish_times)):
        try:
            # Получение название для видео
            title = generate(credentials=gemini)
            # Публикация видео
            youtube(name=video_name, title=title, description=f"meme video #{enum}", publishat=publish_time, credentials=youtube_auth)
            logger.info(f"Видео {title} успешно отправлено на публикацию и опубликуется в {datetime.datetime.fromisoformat(publish_time)}")

            infos.append({"message" : f"Видео {title} успешно отправлено на публикацию в {datetime.datetime.fromisoformat(publish_time)}"})
        except Exception as e:
            logger.error(f"Ошибка в публикации видео {video_name}: {e}")
            infos.append({"message" : f"Ошибка в публикации видео {video_name}: {e}"})
    return infos


# redirect_uris = ["http://localhost"]
# deploy_func(
#     username="balls_productions_inc2",
#     redirect_uris=redirect_uris
# )