import os

def clear_dir(path: str):
    '''
    Функция для очистки директории
    '''
    
    # Проверка существования папки
    if not os.path.exists(path):
        print(f"Директория {path} не существует.")
        return
    
    # Получения списка файлов в папке
    files = os.listdir(path)
    
    # Проходка по каждому файлу
    for file in files:
        #Построение полного пути к файлу
        file_path = os.path.join(path, file)
        try:
            # Проверка - является ли элемент файлом
            if os.path.isfile(file_path):
                # Удаление файла
                os.remove(file_path)
                print(f"Файл {file_path} удален успешно.")
            else:
                print(f"Путь {file_path} не указывает на файл.")
        except Exception as e:
            print(f"Ошибка при удалении файла {file_path}: {e}")