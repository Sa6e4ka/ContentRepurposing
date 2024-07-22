from datetime import datetime, timezone
from typing import Optional, NewType, List

UnixTime = NewType("UnixTime", int)
ISO8601Time = NewType("ISO8601Time", str)


def get_publish_times(
        amount: int, #Количество видео
        interval: int, 
        start_time: Optional[UnixTime]= 0, #Время публикации первого видео
        minutes: Optional[str]= '00' #Минутное время (в публикации первого видео)
) -> List[ISO8601Time]:
    '''
    функция для получения массив, в котором находятся {amount} времен публикаций для видео с установленным интервалом {interval} в формате YouTube_Time(ISO8601)
    '''

    if start_time == 0:
        
        now = datetime.now(timezone.utc).replace(minute=int(minutes), second=0, microsecond=0)
        current_time = int(now.timestamp()) + 86400 + 10800 
    else:
        current_time = start_time
    
    times = [current_time]

    for _ in range(amount - 1):
        times.append(times[-1] + interval * 3600) 

    return [unix_to_iso8601(x) for x in times]


def unix_to_iso8601(unix_timestamp: UnixTime):
    '''
    Функция для перевода unix --> iso
    '''
    dt = datetime.fromtimestamp(unix_timestamp, tz=timezone.utc)
    formatted_time = dt.strftime('%Y-%m-%dT%H:%M:%S.0Z')
    return formatted_time


def iso8601_to_unix(iso8601_time: ISO8601Time):
    '''
    Функция для перевода iso --> unix
    '''
    dt = datetime.strptime(iso8601_time, '%Y-%m-%dT%H:%M:%S.0Z').replace(tzinfo=timezone.utc)
    unix_timestamp = int(dt.timestamp())
    return unix_timestamp
