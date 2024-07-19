import yt_dlp
import json
from datetime import datetime
from Loggs import logger
from typing import Union
import os
from yt_dlp.networking.exceptions import (
    HTTPError,
    NoSupportingHandlers,
    RequestError,
    network_exceptions,
) 


def get_users_videos(username: str, offset: Union[str, int]) -> dict:
    '''
    Функция для получения video_id пользователя

    На выходе получаем словарь {id : duration}
    Перед этим происходит отбор видео по: 
        - Длине (< 50 сек)
        - Коэффициенту (> 0 пока что)
    '''

    # URL профиля автора на TikTok
    url = f'https://www.tiktok.com/@{username}'

    # Опции для извлечения информации
    ydl_opts = {
        'extract_flat': True,  # Извлекать только информацию о видео, не загружая их
        'skip_download': True,  # Пропустить загрузку видео
        "noplaylist" : True
    }           
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=False)
    except network_exceptions or HTTPError or NoSupportingHandlers or RequestError as ex:
        logger.error(f"Error downloading metadata for {username}: {ex}")
        return []

    
    # Получение информации о всех видео автора
    videos = result.get('entries', [])
    
    # Создание словаря {"video_id" : "video_duration"}
    ids_dict = {}

    # Создание словаря с информацией о каждом видео (больше отладочный/для красоты - это офк необязательно) 
    videos_list= []
    videos_info_dict = {
        "username" : username
    }

    # Прозходимся циклом по каждому видео автора
    for enum, video in enumerate(videos):

        # Заканчиваем цикл, если номер итерации равен агрументу offset   
        if type(offset) == int and enum == offset:
            break

        try:
            # Создаем словарик (отладочный) с информацией о видео, котрый потом помещаем в список videos_list
            video_info = {
            "num" : int(enum) + 1,
            "title" : video.get("title"),
            "id" : str(video.get('url').split("/video/")[-1]),
            "duration" :  video.get("duration"),
            "like_count" : video.get("like_count"),
            "view_count" : video.get("view_count"),
            "timestamp" : video.get("timestamp")
            }

            # Пропускаем видео, если одно из значений отсутствует, чтобы не вызвать ошибку
            if any(video_info[key] is None for key in ["duration", "like_count", "view_count", "timestamp"]):
                continue  
            
            # Вычисляем коэффициент like/view_count и выделяем год выпуска видео
            video_info["factor"] = round((int(video_info['like_count']) / int(video_info['view_count'])) * 100, 3)
            year = datetime.fromtimestamp(video_info['timestamp']).year

            # Делаем отбор видео по продолжительности, фактору и году
            if video_info['duration'] <= 50 and video_info["factor"] > 0 and year >= 2020:
                ids_dict[video_info["id"]] = video_info['duration']

                # Если видно отобрано успешно, то помещаем словарь с инфомацией о нем в список
                videos_list.append(video_info)
        except Exception as e:
            logger.error(f"Error processing video {video.get('url')}: {e}")
            continue
    
    # Помещаем список с словариками с информацией о каждом видео в словарь
    videos_info_dict["videos"] = videos_list
    
    with open("jsons/videos_infos.json", "w", encoding="utf-8") as file:
        json.dump(videos_info_dict, file, ensure_ascii=False, indent=4)

    with open("jsons/ids_dict.json", "w", encoding="utf-8") as file:
        json.dump(ids_dict, file, ensure_ascii=False, indent=4)

    return ids_dict





