import datetime
from googleapiclient.errors import HttpError

from .upload import upload_video

def youtube(
        name: str,
        title: str,
        description: str,
        tags: list,
        publishat: datetime, #'2024-07-17T11:23:22.0Z'
        credentials #Получаются функцией authenticate_youtube()
):
    '''
    Функция для выполнения полной авторизации и загрузки видео на YouTube
    '''
    try:
        # Получите авторизованный сервис YouTube API
        youtube = credentials

        # Путь к файлу видео
        file_path = f"{name}"

        # Выполните загрузку видео на YouTube
        upload_video(youtube, file_path, title, description, tags, publishat)

    except HttpError as e:
        error_message = e._get_reason()
        print(f"Произошла ошибка при загрузке видео: {error_message}")