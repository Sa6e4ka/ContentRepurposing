from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from yt_dlp.networking.exceptions import (network_exceptions,HTTPError)

from dotenv import load_dotenv
load_dotenv()

from Loggs import logger

def download_video(data: list) -> list:
    '''
    Функция для загрузки видео по полученному словарю {"video_id" : "duration"}
    '''
    name_list = []
    for item in data:
        name = f'videos/{item}.mp4'

        ydl_opts = {
            'outtmpl': name,
        }
        url = f"https://www.tiktok.com/@tiktok/video/{item}"
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            name_list.append(name)
            logger.info(f"Видео успешно скачано!")
        except network_exceptions or HTTPError or DownloadError as e: # В случае ошибки программа падает и хз ваще как это исправить :/
            logger.error(f"Произошла ошибка при скачивании видео: {e}")
    
    return name_list


def download_single(vid: str):
    
    name = f'videos/{vid}.mp4'

    ydl_opts = {
        'outtmpl': name,
    }
    url = f"https://www.tiktok.com/@tiktok/video/{vid}"
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Видео успешно скачано!")
    except network_exceptions or HTTPError or DownloadError as e: # В случае ошибки программа падает и хз ваще как это исправить :/
        print(f"Произошла ошибка при скачивании видео: {e}")
    
'''
Пример вызова функции
'''
if __name__ == "__main__":
#   download_video(data=...)
    download_single(vid="7340324187547962667")