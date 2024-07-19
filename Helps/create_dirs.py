import os

def create_dirs(dirs_list: list):
    '''
    Создание необходимых директорий
    '''
    for i in dirs_list:
        if not os.path.exists(f"{i}/"):
            os.mkdir(i)

dirs = ["jsons", "output", "videos"]
create_dirs(dirs_list=dirs)
