from config import *
from video_merger import *
from get_videos_from_bucket import *
import json
import random

with open('vid.json') as file:
    json_data = json.load(file)
    ids = [idd for idd in json_data]
    length = len(json_data)



for _ in range(compilation_count):
    compil_path = []
    current_duration = 0
    is_creatable = False
    used = []
    for __ in range(100):
        random_id = random.choice(ids)
        random_duration = json_data[random_id]
        if random_id in used: continue
        used.append(random_id)
        
        if current_duration + random_duration <= time_length:
            current_duration += random_duration
            compil_path.append(f'videos/{random_id}.mp4')
            if current_duration >= 35:
                is_creatable = True
                
                break
    if not is_creatable: continue
    print(compil_path,current_duration)
    
    merge_videos(compil_path,f'output/{_}.mp4')
