import shutil
from Loggs import logger


def remove(directory: str = "videos/") -> None:
    '''
    Функция удаления директории со всеми файлами.
    '''
    try:
        shutil.rmtree(directory)
        logger.info(f"Директория {directory} успешно удалена")
    except OSError as e:
        logger.error("Ошибка при удалении директории:" + e)
