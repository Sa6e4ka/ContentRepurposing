import datetime
from datetime import timedelta

def get_publish_times(start_time: datetime, num_videos: int) -> list:
    """
    Функция для получения списка времени публикаций видео.

    :param start_time: Время начала публикаций
    :param num_videos: Количество видео для публикации
    :return: Список времени публикаций в формате ISO 8601
    """
    publish_times = []
    interval = timedelta(hours=12)  # Интервал между публикациями

    for i in range(num_videos):
        publish_time = start_time + (i * interval)
        publish_times.append(publish_time.isoformat() + 'Z')

    return publish_times

# Пример использования
# start_time = datetime.datetime.now(datetime.UTC)
# num_videos = 6
# publish_times = get_publish_times(start_time, num_videos)

# for time in publish_times:
#     print(time)
# '''
# 2024-07-20T11:12:15.955147+00:00Z
# 2024-07-20T23:12:15.955147+00:00Z
# 2024-07-21T11:12:15.955147+00:00Z
# 2024-07-21T23:12:15.955147+00:00Z
# 2024-07-22T11:12:15.955147+00:00Z
# 2024-07-22T23:12:15.955147+00:00Z
# '''