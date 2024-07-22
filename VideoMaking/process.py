import random

from .remove import remove
from .download import download_video
from .merge import merge_videos

time_length=35
compilation_count=2

def process_video(data: dict, username: str) -> None:
    """
    Функция получения пути видеокарточек их скачивания и объединения
    """
    
    ids = [idd for idd in data]
    length = len(data)
    # Список для списков компилируемых видео 
    paths = []

    for _ in range(compilation_count):
        compile_path = []
        current_duration = 0
        is_creatable = False
        used = []
        for __ in range(length):
            # Случайный выбор видео
            random_id = random.choice(ids)
            # Получение его продолжительности
            random_duration = data[random_id]
            # Если id рандомного видео уже в списке использованных - итерация пропускается
            if random_id in used: continue
            used.append(random_id)
            
            # если сумма текущей длины видео и длины выбранного видео меньше дозволенного, то:
                # Прибавляем к текущей длине видео длину выбранного
                # Помещаем в список подходящих (?) видео названия выбранных видео 
            if current_duration + random_duration <= time_length:
                current_duration += random_duration
                compile_path.append(random_id)
                if current_duration >= 35:
                    is_creatable = True
                    break

        if not is_creatable: continue

        paths.append(compile_path)

    video_names = []

    for k, item_list in enumerate(paths):
        name_list = download_video(data=item_list)

        name = f"output/{username}_{k}.mp4"
        print(name)
        video_names.append(name)

        merge_videos(video_paths=name_list, output_dir=name)
        remove()
    return video_names


